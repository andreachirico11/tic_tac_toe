
game_board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def collect_players_name():
  player_1 = input('give your name player 1: ')
  player_2 = input('give your name player 2: ')
  return player_1,player_2


def draw_grid():
  for i in range(300):
    print(' ')
  f = 0
  while f < len(game_board):
    row = game_board[f]
    output=''
    i = 0
    while i < len(row):
      output += row[i]
      if i < len(row) - 1:
        output += ' | '
      i += 1
    print(output)
    if f < len(row) - 1:
      print('---------')
    f +=1

def check_input(n):
  if n <= 2 and n >= 0:
    return True
  return False

def input_collector(playerN):
  playerInput= input('Your turn player %i: '%playerN)
  inputs = [int(n) for n in playerInput.split()]
  return inputs 

def get_value_from_user(playerN):
  if playerN == 1:
    return 'X'
  else:
    return 'O'

def update_state(playerN, row, col):
  game_board[row][col] = get_value_from_user(playerN)

def play(playerN): 
  x,y = input_collector(playerN)
  if not check_input(x) or not check_input(y) or not game_board[x][y] == ' ':
    return play(playerN)
  update_state(playerN, x, y)

def col_row_checker(obs, value) :
  row_set = set(obs)
  if value in row_set and len(row_set) == 1:
    return True
  return False

def check_winner(playerN):
  value = get_value_from_user(playerN) 
  for row in game_board:
    if col_row_checker(row, value):
      return True  
  for i in range(3):
    temp_col = []
    for row in game_board:
      temp_col.append(row[i])
    if col_row_checker(temp_col, value):
      return True
  diag1 = []
  diag2 = []
  j = 2
  for i in range(3):
    diag1.append(game_board[i][i])
    diag2.append(game_board[j][i])
    j -= 1
  if col_row_checker(diag1, value) or  col_row_checker(diag2, value):
    return True
  return False

def read_file():
  output = {}
  with open('data.txt', 'r') as f:
    for line in f:
      name,points = line.split(':')
      output[name] = int(points)
  return output

def write_file(updated_data):
  with open('data.txt', 'w') as f:
    f.writelines([player+':'+str(updated_data[player]) + '\n' for player in updated_data])

def data_updater(player_name):
  data = read_file()
  if player_name in data.keys():
    data[player_name] += 1
  else:
    data[player_name] = 1
  write_file(data)

def tictac():
  player_1,player_2 = collect_players_name()
  attempts = 0
  winner = ''
  while attempts < 9:
    draw_grid()  
    play(1)
    draw_grid()
    if check_winner(1):
      print("Player 1 has won")
      winner = player_1
      break
    play(2)
    draw_grid()
    if check_winner(2):
      print("Player 2 has won")
      winner = player_2
      break
    attempts += 2
  if winner == '':  
    print('\nDraw')
  else:
    data_updater(winner)




tictac()
