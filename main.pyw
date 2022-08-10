import pygame as pg

pg.init()

#define colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

score = 0
lives = 3

#open window
screen = pg.display.set_mode((800,600))
pg.display.set_caption('Breakout Game')

carryon = True

clock = pg.time.Clock()


#main loop
while carryon:
    #event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            carryon = False


    #game logic


    #drawing code
    screen.fill(DARKBLUE)
    pg.draw.line(screen,WHITE,[0,38],[800,38],2)

    #display score and lives

    font = pg.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))


    pg.display.flip()

    clock.tick(60)



pg.quit()

    
