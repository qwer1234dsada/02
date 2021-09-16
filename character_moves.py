from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
count = 0
angle = 0

while True :
    if count % 2 == 0 :
        while x < 800:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x += 5
            delay(0.01)
        while y < 600:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y += 5
            delay(0.01)
        while x > 0:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x -= 5
            delay(0.01)
        while y > 90:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y -= 5
            delay(0.01)
        count += 1
    else :
        while angle < 360:
            anglex = math.cos(angle * (math.pi/180)) * 300 + 400
            angley = math.sin(angle * (math.pi/180)) * 300 + 300
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(anglex,angley)
            angle += 2
            delay(0.01)
        count += 1
    
close_canvas()
