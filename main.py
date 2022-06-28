# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


# 10 by 10 spots. Rows and columns.
# Color size = 20, space between should be 50
import random
import turtle as t
turq = t.Turtle()
screen = t.Screen()
t.colormode(255)
turq.speed("fastest")
screen.screensize(2000,2000)
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]


def fill_one_line():
    for _ in range(9):
        random_color = random.choice(color_list)
        turq.dot(20, random_color)
        turq.penup()
        turq.forward(50)
        turq.pendown()
    turq.dot(20, random_color)

def move_to_next_line():
    turq.penup()
    turq.left(90)
    turq.forward(50)
    turq.hideturtle()
    turq.left(90)
    for _ in range(9):
        turq.forward(50)
    turq.right(90)
    turq.right(90)
    turq.showturtle()
    turq.pendown()


def draw():
    for _ in range(9):
        fill_one_line()
        move_to_next_line()
    fill_one_line()

draw()










screen.exitonclick()


