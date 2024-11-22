from turtle import Turtle, Screen
import random

from PIL.ImageChops import screen

# import colorgram
# number_of_colors = 20
# color_list = []
# colors = colorgram.extract('hirst_complete_spot_paintings_1024x1024@2x.webp', number_of_colors)
#
# for color in range(number_of_colors):
#     r = colors[color].rgb.r
#     g = colors[color].rgb.g
#     b = colors[color].rgb.b
#     color_tuple = (r,g,b)
#     color_list.append(color_tuple)
#
# print(color_list)
screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.hideturtle()
final_color_list = [(140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (215, 234, 231), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190)]

x_pos = -200
y_pos = -200

for x in range(10):
    for _ in range(10):
        random_color = random.choice(final_color_list)

        tim.penup()
        tim.setpos(x_pos,y_pos)
        tim.dot(20,random_color)
        x_pos += 50

    y_pos +=50
    x_pos = -200










screen.exitonclick()