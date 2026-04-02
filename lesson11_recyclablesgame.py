import pgzrun, random

WIDTH = 800
HEIGHT = 700

#non-recyclable
waste = ["can","paper","bulb","battery"]
score = 0
item = Actor(random.choice(waste))
item.pos = (random.randint(0,775),0)

bin = Actor("bin")
bin.pos = (400,670)

def draw():
    screen.clear()
    screen.fill(color = (0,0,225))
    item.draw()
    bin.draw()
    screen.draw.text("Score: "+ str(score), (0,0),  fontsize = 20 )



pgzrun.go() #dont forget it is a function


