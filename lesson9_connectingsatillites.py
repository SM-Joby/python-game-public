import pgzrun, time, random

WIDTH = 800
HEIGHT = 550

satellites = []
lines = []
no_of_satellites = 10
start_time = 0
end_time = 0
total_time = 0
next_satellite = 0

def create_satellites():
    global start_time
    for i in range(0,no_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = random.randint(50,WIDTH-50), random.randint(50,HEIGHT-50)
        satellites.append(satellite)
    start_time = time.time() #revise time library, time.time shows current time 

def draw():
    global total_time
    screen.blit("space", (0,0))
    number = 1
    for satellite in satellites:
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20), fontsize = 50)
        satellite.draw()
        number = number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if (next_satellite < no_of_satellites):
        end_time = time.time()
        total_time = end_time - start_time
        screen.draw.text(str(round(total_time,1)),(0,350), fontsize = 40)
    else :
        screen.draw.text(str(round(total_time,1)),(0,350),fontsize = 40)

def on_mouse_down(pos):  
    global next_satellite, lines
    if(next_satellite<no_of_satellites):
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append(satellites[next_satellite-1].pos,satellites[next_satellite].pos)
                next_satellite = next_satellite +1
            else:
                lines = []
                next_satellite = 0

create_satellites()
pgzrun.go()











