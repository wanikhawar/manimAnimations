from manim import *

class square_to_circle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(RED, opacity=0.5) # set color and transparency

        square = Square() # create a square
        square.rotate(PI/4) # rotate by PI/4 radians

        self.play(Create(square)) # animate the creation of the square
        self.play(Transform(square, circle)) # interpolate the square into the circle
        self.play(FadeOut(square)) # fade out animation
        