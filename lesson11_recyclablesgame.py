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
    screen.fill(color = (0,0,225))# brackets are given since the rgb numbers are tuple
    item.draw()
    bin.draw()
    screen.draw.text("Score: "+ str(score), (0,0),  fontsize = 20 )

def update():
    global item,score
    item.y = item.y+4

    if keyboard.left:
        bin.x = bin.x-2
    elif keyboard.right:
        bin.x = bin.x+2
    
    if bin.colliderect(item):
        if item.image == "can":
            score = score+10
        elif item.image == "paper":
            score = score+10
        elif item.image == "bulb":
            score = score-10
        elif item.image == "battery":
            score = score-10
    
        item = Actor(random.choice(waste))
        item.pos = (random.randint(0,775),0)

    if item.y>HEIGHT:
        item = Actor(random.choice(waste))
        item.pos = (random.randint(0,775),0)
        


pgzrun.go() #dont forget it is a function


