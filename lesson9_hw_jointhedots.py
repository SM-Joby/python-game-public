import pgzrun, time, random

WIDTH = 800
HEIGHT = 550

dots = []
lines = []
no_of_dots = 10
start_time = 0
end_time = 0
total_time = 0
next_dot = 0

def create_dots():
    global start_time
    for i in range(0,no_of_dots):
        dot = Actor("dot")
        dot.pos = random.randint(50,WIDTH-50), random.randint(50,HEIGHT-50)
        dots.append(dot)
    start_time = time.time()  

def draw():
    global total_time
    screen.blit("dotsbg", (0,0))
    number = 1
    for dot in dots:
        screen.draw.text(str(number),(dot.pos[0],dot.pos[1]+20), fontsize = 50)
        dot.draw()
        number = number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if (next_dot < no_of_dots):
        end_time = time.time()
        total_time = end_time - start_time
        screen.draw.text(str(round(total_time,1)),(50,50), fontsize = 40)
    else :
        screen.draw.text(str(round(total_time,1)),(50,50),fontsize = 40)

def on_mouse_down(pos):  
    global next_dot, lines
    if(next_dot<no_of_dots):
        if dots[next_dot].collidepoint(pos):
            if next_dot:
                lines.append(dots[next_dot-1].pos,dots[next_dot].pos)
                next_dot = next_dot +1
            else:
                lines = []
                next_dot = 0

create_dots()
pgzrun.go()

















