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
    board_width = data.get('width') 
    board_height = data.get('height') 
    path = 0
    
    board = [[0 for x in xrange(board_height+2)] for y in xrange(board_width+2)]

    # TODO: Do things with data

    #setup Safe value
    for row in range(board_height+2):
	for col in range(board_width+2):
	    board[row][col] = SAFE
	
    # set up Wall value	
    for row in range(board_height+2):
       board[row][0] = ENEMY    # Left wall
       board[row][board_width+1] = ENEMY    # Right wall
    for col in range(board_width+2):
       board[0][col] = ENEMY    # Top wall
       board[board_height+1][col] = ENEMY   # Bottom wall

    ranlen = len(data['you']['body']['data'])
    #set the self-sanke body as the enemy
    for num in range(ranlen):
	posx = data['you']['body']['data'][num]['x'] + 1     
	posy = data['you']['body']['data'][num]['y'] + 1
	board[posx][posy] = ENEMY
	    
    #get the position of the snake head
    sx = data['you']['body']['data'][0]['x'] + 1      
    sy = data['you']['body']['data'][0]['y'] + 1

    if board[sx+1][sy] == SAFE or board[sx+1][sy] == WALL:
        print "sx+1:",sx+1
        print "sy:",sy
	path = 3
    elif board[sx-1][sy] == SAFE or board[sx-1][sy] == WALL:
        print "sx-:",sx-1
        print "sy:",sy
	path = 2
    elif board[sx][sy+1] == SAFE or board[sx][sy-1] == WALL:
        print "sx:",sx
        print "sy-1:",sy+1
	path = 1
    elif board[sx][sy-1] == SAFE or board[sx][sy+1] == WALL:
        print "sx:",sx
        print "sy+1:",sy-1
    	path = 0

    directions = ['up', 'down', 'left', 'right']
    print directions[path]
    return {
        'move': directions[path],
        'taunt': 'I\'m drunk'
    } 
	    
    
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
