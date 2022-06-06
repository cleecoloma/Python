##DRAW A SQUARE
# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# for i in range (4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

##DRAW DASHED LINES
# import turtle as t

# tim = t.Turtle()
# for i in range(10):
#     tim.down()
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)

##DRAW SHAPES
# import turtle as t
# import random

# tim = t.Turtle()
# colors = ["gray", "blue", "green", "yellow", "pink", "red", "black", "brown", "orange", "purple"]
# color = 0
# sides = 3
# for i in range(8):
#     tim.pencolor(colors[color])
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)
#     sides += 1
#     color += 1


##RANDOM WALK
# import turtle as t
# import random

# tim = t.Turtle()
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# pick_degrees = ["0", "90", "-90", "180"]

# def rng_choice(pick_turn):
#     tim.forward(30)
#     tim.right(pick_turn)

# end_game = False
# while not end_game:
#     tim.pensize(10)
#     tim.speed(3)
#     tim.color(random.choice(colours))
#     rng_choice(int(random.choice(pick_degrees)))

# #RANDOM COLOR
# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)   
#     return (r, g, b)

# pick_degrees = ["0", "90", "-90", "180"]
# def rng_choice(pick_turn):
#     tim.forward(30)
#     tim.right(pick_turn)

# end_game = False
# while not end_game:
#     tim.pensize(10)
#     tim.speed(3)
#     tim.color(random_color())
#     rng_choice(int(random.choice(pick_degrees)))


#SPIROGRAPH
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
number = 0
for i in range(100):
    tim.speed(0)
    tim.pensize(3)
    tim.circle(100)
    tim.color(random_color())
    tim.setheading(number)
    number += 10
    
screen = t.Screen()
screen.exitonclick
    