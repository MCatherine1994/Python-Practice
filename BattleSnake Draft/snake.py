import bottle
import os
import random
from random import randint

ENEMY = 1
WALL = 2
SAFE = 5
#---------------------------------------------------------------------------
game_id = ''
board_width = 0
board_height = 0
board = [[0 for x in range(board_width)] for y in range(board_height)] 
secure_level = [[0 for x in range(board_width)] for y in range(board_height)] 
#security level:
#	0: Emergence - Can't move to this location
#	1: Not secure - forcase onestep (after move one step, has level 0 around ourself)
#	2: Maybe secure - forcase twostep (after move two step, has level 0 around ourself)
#	3: Normal - forcase threestep (after move three step, has level 0 around ourself)
#	4: Secure - forcase fourstep
#	5: Gold - forcase didn't reach the area
#---------------------------------------------------------------------------

@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    global game_id
    global board_width
    global board_height
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')

    head_url = '%s://%s/static/head2.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'cc',
        "head_type": "tongue",
        "tail_type": "pixel"
    }
                            


@bottle.post('/move')
def move():
    data = bottle.request.json

    #crate a 2d array for board: all values are 0
    global board
	global secure_level
    board = [[0 for x in range(board_width)] for y in range(board_height)] 
	secure_level = [[0 for x in range(board_width)] for y in range(board_height)] 
	
	for x in range(board_width)
		for y in range(board_height)
			secure_level[x][y] = 5

    #get food location
    my_food_list = []
    food_list = data.get('food')['data']
    for each_food in food_list:
        food_x = each_food['x']
        food_y = each_food['y']
        my_food_list.append([food_x, food_y]) #my_food_list e.g. [[12,1], [23,12], [0,9]]

    #get the location of myself
    my_body_list = []
    body_list = data.get('you')['body']['data']
    my_len = data.get('you')['length']
    print "my_len:", my_len
    for each_segment in body_list:
        segment_x = each_segment['x']
        segment_y = each_segment['y']
        my_body_list.append([segment_x,segment_y]) #my_body_list e.g. [[1,1], [2,1], [2,2], 3] #first coor is the head!!
    my_body_list.append(my_len)
    #print "my_body_list:", my_body_list

    #get the location of other snakes   (TODO!!!)
    enemy_body_list = []
    enemy_list = data.get('snakes')['data']
    for each_enemy in enemy_list:
        each_enemy_snake = []
        each_enemy_len = each_enemy['length']
        for each_enemy_segement in each_enemy['body']['data']:
            enemy_body_x = each_enemy_segement['x']
            enemy_body_y = each_enemy_segement['y']
            each_enemy_snake.append([enemy_body_x, enemy_body_y])
        enemy_body_list.append(each_enemy_len) #enemy_body_list e.g [ [[2,3],[2,4],2], [[5,6],[5,7],[5,8],3] ]  two snakes
    
    #set the value of walls to be 1 (including my body and enemy snakes' bodies)
    board = set_walls(my_body_list, enemy_body_list, board)

    #get the position of the snake head
    head = my_body_list[0] #e.g.[1,1]

    #get the optional directions for the head
    directions = direction_options(head)
    
    #TODO!!!
    direction = find_best_direction(directions, head, my_food_list)

    
    return {
        'move': direction,
        'taunt': 'I\'m drunk'
    } 

#the coor for walls are [1], the body of our snake, the enemy snake, and the security level of these location are 0
def set_walls(my_body_list, enemy_body_list, board):
    global board
	global secure_level
    for each_segment in my_body_list[:-1]:  #[1,1]
        segx = each_segment[0]
        segy = each_segment[1]
        board[segx][segy] = 1
		secure_level[segx][segy] = 0
		
    for each_snake in enemy_body_list:
		for each_segment in each_snake[:-1]:
			segx = each_segment[0]
			segy = each_segment[1]
			board[segx][segy] = 1
			secure_level[segx][segy] = 0
	
	#reset the board value of the enemy snake head if the enemy snake length is less than our snake
	for each_enemy in enemy_body_list:
		enemy_head = []
		if each_enemy[-1] < my_body_list[-1]:
			enemy_head.append(each_enemy[0][0])
			enemy_head.append(each_enemy[0][1])
			head_next_location = next_move_location(enemy_head)
			#might return several possible location, so check each location
			for next in head_next_location:
				segx = next[0]
				segy = next[1]
			board[segx][segy] = 0
			
    return board

#get the location of next move
def next_move_location(current_location):
	global board
	next_location = []
	directions = direction_options(current_location)
	for next_move in directions:
		if next_move == 'up'
			next_location.append([current_location[0],current_location[1]-1])
		elif next_move == 'down'
			next_location.append([current_location[0],current_location[1]+1])
		elif next_move == 'left'
			next_location.append([current_location[0]-1,current_location[1]])
		elif next_move == 'right'
			next_location.append([current_location[0]+1,current_location[1]])
	return next_location
	
	
#get the direction options of my snake head 
def direction_options(head):
    global board
    global board_width
    global board_height
    curx = head[0]
    cury = head[1]
    directions = []
    #check if we can move up
    if cury >= 1:
        if board[curx][cury-1] == 0:
             directions.append('up')
    #check if we can move right
    if curx <= board_width - 2:
        if board[curx+1][cury] == 0:
             directions.append('right')
    #check if we can move left
    if curx >= 1:
        if board[curx-1][cury] == 0:
             directions.append('left')
    #check if we can move down
    if cury <= board_height - 2:
        if board[curx][cury+1] == 0:
             directions.append('down')
    return directions

#TODO
def find_best_direction(directions, head, my_food_list):
    direction = ''
    food_pos = my_food_list[0] #e.g.[3,7]
    headx = head[0]
    heady = head[1]
    foodx = food_pos[0]
    foody = food_pos[1]
    updistance, rightdistance, downdistance, leftdistance = float("inf"),float("inf"),float("inf"),float("inf") 

    for legal_direction in directions:
        if legal_direction == 'up':
            updistance = (headx-foodx)**2 + (heady-1-foody)**2
        elif legal_direction == 'right':
            rightdistance = (headx+1-foodx)**2 + (heady-foody)**2
        elif legal_direction == 'left':
            leftdistance = (headx-1-foodx)**2 + (heady-foody)**2
        elif legal_direction == 'down':
            downdistance = (headx-foodx)**2 + (heady+1-foody)**2

    print(updistance, rightdistance, downdistance, leftdistance)
    direction= 'up'
    min_distance = updistance
    if rightdistance<min_distance:
        direction = 'right'
        min_distance = rightdistance
    if downdistance<min_distance:
        direction='down'
        min_distance = downdistance
    if leftdistance<min_distance:
        direction='left'
        min_distance = leftdistance
    return direction
	
	
#get the new location of the enemy snake
def get_new_enemy_body_list(enemy_body_list):
	for each_snake in enemy_body_list:
		for each_segment in range(len(each_snake)-1):
			if each_segment == 0:
				

	
#compare which next_move_location has the higher secure_level	
def set_security(self_head, enemy_body_list, round):
	global board
	global secure_level
	forcast_board = [[0 for x in range(board_width)] for y in range(board_height)] 
	#first find the next possible location for our snake head
	self_next_location = next_move_location(self_head)
	new_enemy_body_list = get_new_enemy_body_list(enemy_body_list)
	
	
	#for each of the next location, check the up,down,left,right to see if there is an enemy 
	for next_location in self_next_location:
		segx = next_location[0]
		segy = next_location[1]
		#check the right and check if it is the original head
		if board[segx+1][segy] == 1 and segx+1 != self_head[0]:
			secure_level[segx][segy] = round  #(pass 1 if test the first step, add one after each round)
		#check the left and check if it is the original head	
		elif board[segx-1][segy] == 1 and segx-1 != self_head[0]:
			secure_level[segx][segy] = round 
		#check the up and check if it is the original head
		elif board[segx][segy-1] == 1 and segy-1 != self_head[0]:
			secure_level[segx][segy] = round	


@bottle.post('/end')
def end():
    data = bottle.request.json
    return {'taunt': 'uh'}


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)


