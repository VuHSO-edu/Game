import pygame as pg
import random

pg.init()
#Tạo cửa sổ game (Windown game)

screen = pg.display.set_mode((400,400))
pg.display.set_caption('Snake Game')
#Var
score=highscore=0
Snake_than = 20 # Thân rắn
x=y=200
x_change=y_change=0
body_snake=[]
length=1
#Thức ăn cho rắn (Create food)
food_x=random.randint(0,19)*Snake_than
food_y=random.randint(0,19)*Snake_than
#Tốc độ của rắn (Speed Snake)
clock = pg.time.Clock()
speed_snake=3
#Def function
def check_col():
    if x < 0 or x > 400 or y < 0 or y > 400 or (x,y) in body_snake[:-1]:
        return False
    return True
def ScoreView():
    font=pg.font.Font(None,36)
    if gameplay:
        score_txt=font.render(f'Score:{score}',True,(255,255,255))
        screen.blit(score_txt,(0,0))
        hscore_txt=font.render(f'High Score:{highscore}',True,(255,255,255))
        screen.blit(hscore_txt,(170,0))
    else:
        note_txt=font.render(f'Nhấn phím cách để chơi lại',True,(255,255,255))
        screen.blit(note_txt,(170,0))
#Thiết lập game (Game Loop)

gameplay=True

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
            quit()
        #Điều khiển rắn(Snake move)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_change-=Snake_than
                y_change=0
            elif event.key == pg.K_RIGHT:
                x_change=Snake_than
                y_change=0
            elif event.key == pg.K_UP:
                x_change=0
                y_change-=Snake_than
            elif event.key == pg.K_DOWN:
                x_change=0
                y_change=Snake_than
            elif event.key == pg.K_SPACE:
                gameplay=True
    #Clear screen
    screen.fill((0,0,0))
    ScoreView()
    if gameplay == True:
        #Update Snake position(Cập nhật vị trí của rắn)
        x+=x_change
        y+=y_change
        #Add Snake Part(Thêm thân rắn)
        body_snake.append((x,y))
        #Remove Snake Part
        if len(body_snake) > length:
            del body_snake[0]
        #Check Snake eat food 
        if x==food_x and y==food_y:
            length+=1
            score+=1
            if score > highscore: highscore=score
            #Cho xuất hiện lại Food Snake
            food_x=random.randint(0,19)*Snake_than
            food_y=random.randint(0,19)*Snake_than
        #Vẽ thân rắn(Draw Snake)
        for x,y in body_snake:
            pg.draw.rect(screen,(255,255,255),(x,y,Snake_than,Snake_than))
        #Vẽ đồ ăn cho rắn(Draw food)
        pg.draw.rect(screen,(255,0,0),(food_x,food_y,Snake_than,Snake_than))
        gameplay=check_col()
        clock.tick(speed_snake)
    else:
        #Reset game
        x=y=200
        x_change=y_change=0
        body_snake=[]
        length=1
        score=1

    # Update screen
    pg.display.update()
    

    