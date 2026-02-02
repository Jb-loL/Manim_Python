from manim import *
import numpy as np

class CircleAreaRectangleMethod(Scene):
    def construct(self):
        r = 2
        n = 24

        # Title
        title = Text("Area of a Circle (Rectangle Method)", font_size=30)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        # Circle
        circle_center = LEFT * 3
        circle = Circle(radius=r).move_to(circle_center)
        self.play(Create(circle))

        # Vertical pieces inside the circle
        pieces = VGroup()
        dx = (2 * r) / n

        for i in range(n):
            x = -r + i * dx + dx / 2
            h = 2 * np.sqrt(r**2 - x**2)

            piece = Rectangle(
                width=dx,
                height=h,
                stroke_width=0,
                fill_opacity=0.7
            )
            piece.move_to(circle_center + RIGHT * x)
            pieces.add(piece)

        self.play(LaggedStartMap(FadeIn, pieces, lag_ratio=0.03))
        self.wait(1)

        self.play(FadeOut(circle))

        # Target rectangle parameters
        rect_center = RIGHT * 3
        rect_height = r
        rect_width = PI * r * 0.9

        x_start = rect_center[0] - rect_width / 2
        x_step = rect_width / n

        # Create UNIFORM rectangles as targets
        targets = VGroup()
        for i in range(n):
            uniform = Rectangle(
                width=x_step,
                height=rect_height,
                stroke_width=0,
                fill_opacity=0.7
            )
            x = x_start + i * x_step
            uniform.move_to([x, rect_center[1], 0])
            targets.add(uniform)

        # Transform pieces into uniform rectangles
        self.play(
            LaggedStart(
                *[Transform(pieces[i], targets[i]) for i in range(n)],
                lag_ratio=0.03,
                run_time=3
            )
        )

        # Rectangle outline
        outline = Rectangle(
            width=rect_width,
            height=rect_height,
            stroke_color=YELLOW,
            stroke_width=3
        ).move_to(rect_center)

        self.play(Create(outline))

        # Labels
        base_label = MathTex(r"\text{Base} \approx \pi r", font_size=32)
        base_label.next_to(outline, DOWN, buff=0.2)

        height_label = MathTex(r"\text{Height} = r", font_size=32)
        height_label.next_to(outline, RIGHT, buff=0.2)

        self.play(Write(base_label), Write(height_label))

        # Final formula
        formula = MathTex(r"A = \pi r^2", font_size=36)
        formula.next_to(outline, UP, buff=0.25)
        self.play(Write(formula))

        self.wait(2)
