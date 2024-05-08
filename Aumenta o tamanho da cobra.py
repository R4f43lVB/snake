snake.insert(0,list(pos))
if pos[0][1]==pos_fruta[0][1]:
    pontos+=100
    spawn=False
else:
    snake.pop()
if spawn==False:
    posicao_fruta=[random.randrange(1,(window_x//10))*10,
                   random.randrange(1,(window_y//10))*10]
spawn=True
game_window.fill(black)