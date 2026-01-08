import pgzrun

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
    screen.draw.text("score" + str(score),center = (50,450), fontsize = 50) # center does
 
#background
#to give a background image we give screen.blit()



pgzrun.go()