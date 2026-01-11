from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
     #Food Appearances
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        #Location of the will change randomly as the eats
        ramdom_x = random.randint(-280, 280)
        random_y =random.randint(-280, 280)
        self.goto(ramdom_x, random_y)
