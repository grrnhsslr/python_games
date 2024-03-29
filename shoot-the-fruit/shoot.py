# must be running in terminal "pgzrun shoot.py"
import random


apple = Actor('apple')
WIDTH = 900
HEIGHT = 400


def draw():
    screen.clear()
    apple.draw()
    
def place_apple():
    apple.x = random.randint(10, 300)
    apple.y = random.randint(10, 200)

    
place_apple()


def on_mouse_down(pos):
    score = 0
    if apple.collidepoint(pos):
        score += 1
        place_apple()
    else:
        print('you missed')
        quit()
    print(f'Good job! Your score: {score}')
