import pgzrun, random

WIDTH = 500
HEIGHT = 500

TITLE = "Bumble bee"
bee = Actor("bee")
flower = Actor("flower")
bee.pos = (200,200)
flower.pos = (350,300)

score = 0
game_over = False

def draw():
    screen.clear()
    screen.blit("beebackground",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score" + str(score),center = (100,450), fontsize = 35) # center makes the middle of your text start at the point you have written

    if (game_over == True):
        screen.fill(color = (255,0,0))
        screen.draw.text("TIME IS UP!!!", (250,250), fontsize = 50)

def flower_placing():
    flower.x = random.randint(50,450)
    flower.y = random.randint(50,450)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left :
        bee.x = bee.x - 2
    elif keyboard.right :
        bee.x = bee.x + 2
    elif keyboard.up :
        bee.y = bee.y - 2
    elif keyboard.down :
        bee.y = bee.y + 2
    
    flower_collected = bee.colliderect(flower) # collidepoint is used for mouse, colliderect is between two actors
    if flower_collected == True :
        score = score + 10
        flower_placing()

clock.schedule(time_up, 60.0)


#background
#to give a background image we give screen.blit()



pgzrun.go()