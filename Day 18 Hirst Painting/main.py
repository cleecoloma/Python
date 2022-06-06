# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)

color_list = [
(188, 151, 176), (166, 73, 29), (38, 97, 176), (22, 94, 14), (219, 213, 207), (51, 118, 45), (146, 72, 102), 
(11, 72, 7), (149, 24, 8), (194, 141, 26), (222, 200, 211), (206, 209, 215), (199, 159, 116), (171, 99, 134), 
(211, 179, 195), (208, 216, 210), (132, 24, 41), (143, 165, 198), (84, 31, 6), (68, 122, 201), (195, 91, 77), 
(152, 179, 151), (76, 82, 13), (93, 13, 29), (15, 60, 141), (88, 154, 81), (219, 197, 137), (181, 186, 212), 
(220, 177, 171), (20, 43, 81)
]
timmy.speed("fastest")
timmy.penup()
timmy.goto(-250, -250)
timmy.hideturtle()

def dot():
    color = random.choice(color_list)
    # timmy.pencolor(color)
    # timmy.fillcolor(color)
    timmy.dot(20, color)


add_space = -250
def row():
    global add_space
    add_space += 50
    timmy.goto(-250, add_space)
    
for i in range(10):
    for i in range(10):
        dot()
        timmy.forward(50)
    row()

turtle.exitonclick()
