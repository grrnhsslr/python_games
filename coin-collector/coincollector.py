# must be running in terminal "pgzrun coincollector.py"
from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
gameover = False
fox = Actor('fox')
fox.pos = 100, 100

coin = Actor('coin')
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if gameover:
        screen.fill('pink')
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)
                     
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
    

def time_up():
    global gameover
    gameover = True
    clock.schedule(time_up, 7.0)

def update():
    global score

    
    if keyboard.left:
        fox.x = fox.x - 4
        
    elif keyboard.right:
        fox.x = fox.x + 4

    elif keyboard.up:
        fox.y = fox.y - 4

    elif keyboard.down:
        fox.y = fox.y + 4
     
   
    coin_collected = fox.colliderect(coin)


    if coin_collected:
        score = score + 10
        place_coin()

clock.schedule(time_up, 7.0)
place_coin()
    
