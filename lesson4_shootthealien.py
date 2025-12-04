import pgzrun, random

WIDTH = 500
HEIGHT = 500

TITLE = "Shoot the Alien"
alien = Actor("alien")
message = "hi"
#alien.pos = (50,50)
def draw():
    screen.clear()
    screen.fill(color = (0,0,200)) # RGB colour code # .fill is for background
    alien.draw()
    screen.draw.text(message,center = (400,10), fontsize = 30)

def placing_alien():
    alien.x=random.randint(50,450)
    alien.y=random.randint(50,450)
    
def on_mouse_down(pos):
    global message # making something global makes it accessable everywhere
    if alien.collidepoint(pos):
        message = "good shot"
        placing_alien()
    else:
        message = "bad shot"

placing_alien()
    

pgzrun.go()