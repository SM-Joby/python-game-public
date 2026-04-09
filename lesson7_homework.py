import pgzrun, random

WIDTH = 800
HEIGHT = 800

TITLE = "Tom and jerry"
tom = Actor("tom")
jerry = Actor("jerry")
tom.pos = (200,200)
jerry.pos = (350,300)

score = 0
game_over = False

def draw():
    screen.clear()
    screen.fill(color = (0,0,255))
    tom.draw()
    jerry.draw()
    screen.draw.text("score" + str(score),center = (50,450), fontsize = 50) 
    
    if (game_over == True):
        screen.fill(color = (255,0,0))
        screen.draw.text("TIME IS UP!!!", (250,250), fontsize = 50)

def jerry_placing():
    jerry.x = random.randint(50,750)
    jerry.y = random.randint(50,750)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        tom.x = tom.x - 2
    elif keyboard.right:
        tom.x = tom.x + 2
    elif keyboard.up:
        tom.y = tom.y - 2
    elif keyboard.down:
        tom.y = tom.y + 2

    jerry_caught = tom.colliderect(jerry)
    if jerry_caught == True :
        score = score + 10
        jerry_placing()

clock.schedule(time_up,60.0)


pgzrun.go()