from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 운동 코드
def rectangle_movement():
    x = 400
    while (x < 770):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    y = 90
    while (y < 550):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(770, y)
        y = y + 2
        delay(0.01)

    x = 770
    while (x > 30):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 550)
        x = x - 2
        delay(0.01)

    y = 550
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(30, y)
        y = y - 2
        delay(0.01)

    x = 30
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

# 원 운동 코드
def circle_movement():
    cx, cy = 400, 300
    r = 200
    angle = 270

    while angle > -90:
        x = cx + r * math.cos(math.radians(angle))
        y = cy + r * math.sin(math.radians(angle))
        
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        
        angle -= 2
        delay(0.01)

while True:
    rectangle_movement()  # 사각형 운동
    circle_movement()     # 원 운동
