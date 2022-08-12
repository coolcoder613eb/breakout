import pygame as pg
from paddle import Paddle
from ball import Ball
from brick import Brick

pg.init()

#define colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)

score = 0
lives = 3

#open window
screen = pg.display.set_mode((800,600))
pg.display.set_caption('Breakout Game')


#sprites

asl = pg.sprite.Group()

paddle = Paddle(LIGHTBLUE,100,10)
paddle.rect.x = 350
paddle.rect.y = 585


ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

ab = pg.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    asl.add(brick)
    ab.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    asl.add(brick)
    ab.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    asl.add(brick)
    ab.add(brick)

asl.add(paddle)
asl.add(ball)

carryon = True

clock = pg.time.Clock()


#main loop
while carryon:
    #event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            carryon = False
        elif event.type==pg.KEYDOWN:
                if event.key==pg.K_x: #Pressing the x Key will quit the game
                     carryOn=False

    #move paddle
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        paddle.moveleft(8)
    if keys[pg.K_RIGHT]:
        paddle.moveright(8)


    #game logic
    asl.update()

    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pg.font.Font('broadw.ttf',74)
            text = font.render('GAME OVER',1,RED)
            screen.blit(text,(150,300))
            pg.display.flip()
            pg.time.wait(3000)
            carryon = False
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]

    if pg.sprite.collide_mask(ball,paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()


    bcl = pg.sprite.spritecollide(ball,ab,False)
    for brick in bcl:
      ball.bounce()
      score += 1
      brick.kill()
      if len(ab)==0:
           #Display Level Complete Message for 3 seconds
            font = pg.font.Font('broadw.ttf', 74)
            text = font.render('LEVEL COMPLETE', 1, GREEN)
            screen.blit(text, (50,300))
            pg.display.flip()
            pg.time.wait(3000)
 
            #Stop the Game
            carryon=False


    #drawing code
    screen.fill(DARKBLUE)
    pg.draw.line(screen,WHITE,[0,38],[800,38],2)

    #display score and lives

    font = pg.font.Font('freesansbold.ttf', 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,5))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,5))

    #draw sprites
    asl.draw(screen)


    #update screen
    pg.display.flip()


    clock.tick(60)



pg.quit()

    
