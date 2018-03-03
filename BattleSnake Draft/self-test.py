snake = {
    'data': [
      {
        'body': {
          'data': [
            {
              'x': 13,
              'y': 19
            },
            {
              'x': 13,
              'y': 19
            },
            {
              'x': 13,
              'y': 19
            }
          ],
          'object': 'list'
        },
        'health': 100,
        'id': '58a0142f-4cd7-4d35-9b17-815ec8ff8e70',
        'length':3
      },
      {
        'body': {
          'data': [
            {
              'x': 8,
              'y': 15
            },
            {
              'x': 8,
              'y': 15
            },
            {
              'x': 8,
              'y': 15
            }
          ],
          'object': 'list'
        },
        'health': 100,
        'id': '48ca23a2-dde8-4d0f-b03a-61cc9780427e',
        'length':3
      }
    ],
    'object': 'list'
  }
  
enemy_body_list = []
each_enemy_len = 0

for each_enemy in snake['data']:
    each_enemy_len = each_enemy['length']
    each_enemy_snake = []
    for each_enemy_segement in each_enemy['body']['data']:
        enemy_body_x = each_enemy_segement['x']
        enemy_body_y = each_enemy_segement['y']
        each_enemy_snake.append([enemy_body_x, enemy_body_y])
    each_enemy_snake.append(each_enemy_len)  
    enemy_body_list.append(each_enemy_snake)  
print  each_enemy_snake  
print enemy_body_list
