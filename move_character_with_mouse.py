from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def random_hand_point():
    return random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

def move_character(point_x, point_y):
    global x, y, arrow_x, arrow_y, dir

    if x < point_x:
        dir = 1
    else:
        dir = -1

    t = 0.03
    x = (1 - t) * x + t * point_x
    y = (1 - t) * y + t * point_y

    dis = math.sqrt( (point_x - x) ** 2 + (point_y - y) ** 2 )
    if dis < 5:
        arrow_x, arrow_y = random_hand_point()

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir = 1
arrow_x, arrow_y = random_hand_point()
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    move_character(arrow_x, arrow_y)

    arrow.draw(arrow_x, arrow_y)
    if dir == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dir == -1:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.01)

close_canvas()




