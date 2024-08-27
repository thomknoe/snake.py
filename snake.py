import turtle
import random

width = 500
height = 500
delay = 100
food_size = 10

offsets = {
    "up": (0,20),
    "down": (0,-20),
    "left": (-20,0),
    "right": (20,0)
}


def bind_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")


def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":
            snake_direction = "up"

    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"

    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"
            
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"


def game_loop():
    brush.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    if new_head in snake or new_head[0] < - width / 2 or new_head[0] > width / 2 \
        or new_head[1] < - height / 2 or new_head[1] > height / 2:
        reset()

    else:
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)

        for body in snake:
            brush.goto(body[0],body[1])
            brush.stamp()

        screen.title(f"Snake Game — Score: {score}")
        screen.update()
        turtle.ontimer(game_loop, delay)


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint( - width / 2 + food_size, width / 2 - food_size)
    y = random.randint( - height / 2 + food_size, height / 2 - food_size)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0,0],[20,0],[40,0],[60,0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()


screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
bind_keys()

brush = turtle.Turtle()
brush.shape("square")
brush.color("white")
brush.penup()

food = turtle.Turtle()
food.shape("square")
food.color("white")
food.shapesize(food_size / 20)
food.penup()

reset()

turtle.done()