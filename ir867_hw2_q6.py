# Indra 
# CS - UY 1114
# 24 Sept 2018
# Homework 2
import math
import turtle
import random
beta_angle = random.randint(0,179)
alpha_angle = (180-beta_angle)/2
side_a_length=100
side_b_length= (((math.sin(math.radians(beta_angle)))*side_a_length)/(math.sin(math.radians(alpha_angle))))


turtle.forward(side_b_length)
turtle.left(180-alpha_angle)
turtle.forward(side_a_length)
turtle.left(180-beta_angle)
turtle.forward(side_a_length)                                                                   



                                                                
