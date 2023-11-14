from manim import *


class Positioning(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.rotate(PI / 4)

        square.next_to(circle, RIGHT, buff=1)
        self.play(Create(square), Create(circle))

