from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
import math

x=400
y=90
while (x > 0, y > 0):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x = x + math.radians(30)
    y = y + math.radians(90)
    delay(0.01)

x = 400
while (x < 770):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)

y=90
while (y < 550):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(770, y)
    y = y + 2
    delay(0.01)

x=770
while (x > 30):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 550)
    x = x - 2
    delay(0.01)

y=550
while (y > 90):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(30, y)
    y = y - 2
    delay(0.01)
    
x=30
while (x < 400):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)
    
close_canvas()

math.radians(90)

