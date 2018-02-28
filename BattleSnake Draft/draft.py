import bottle
import os
import random

ENEMY = 1
WALL = 2
SAFE = 5

from random import randint

@bottle.post('/move')
def move():
    data = bottle.request.json
#-------------------add code-------------------------------------------------------------------#	
	board_width = data.get('width')
    	board_height = data.get('height')
	
	board = [[0 for x in xrange(board_height)] for y in xrange(board_width)]

	#setup Safe value
	for row in range(board_height):
		for col in range(board_width):
			board[row][col] = SAFE
	
	# set up Wall value	
	for row in range(board_height):
		board[row][0] = WALL    # Left wall
		board[row][board_width] = WALL    # Right wall
	for col in range(board_width):
		board[0][col] = WALL    # Top wall
		board[board_height][col] = WALL   # Bottom wall
	
	#set the self-sanke body as the enemy
	for index in range(len(data['you']['body']['data']))
		posx = data['you']['body']['data'][index]['x']      
		posy = data['you']['body']['data'][index]['y']
		board[posx][poxy] = ENEMY
	
	#get the position of the snake head
	sx = data['you']['body']['data'][0]['x']      
	sy = data['you']['body']['data'][0]['y']
	
	#if snake head is at the wall position 
	if board[sx][sy] == WALL:
		if board[sx+1][sy] == SAFE:    
			path = 3
		elif board[sx-1][sy] == SAFE:
			path = 2
		elif board[sx][sy-1] == SAFE:
			path = 1
		elif board[sx][sy+1] == SAFE:
			path = 0
	else:
		path = randint(0,3)

    # TODO: Do things with data
    
    directions = ['up', 'down', 'left', 'right']    
    print directions[path]
    return {
        'move': directions[path],
        'taunt': 'battlesnake-python!'
    }
	
	
	
	
