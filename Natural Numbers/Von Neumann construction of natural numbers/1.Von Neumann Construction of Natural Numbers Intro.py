from manim import *

class VonNeumannNaturals(Scene):
    def construct(self):

        title = Text("von Neumann Construction of Natural Numbers", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))

        zero = MathTex(r"0 := \varnothing", font_size=38)
        zero.next_to(title, DOWN, buff=0.8)
        self.play(Write(zero))
        self.wait(0.8)

        successor = MathTex(
            r"S(n) := n \cup \{n\}",
            font_size=38
        )
        successor.next_to(zero, DOWN, buff=0.6)
        self.play(Write(successor))
        self.wait(1)

        numbers = VGroup(
            MathTex(r"0 = \varnothing", font_size=34),
            MathTex(r"1 = \{\varnothing\}", font_size=34),
            MathTex(r"2 = \{\varnothing, \{\varnothing\}\}", font_size=34),
            MathTex(
                r"3 = \{\varnothing, \{\varnothing\}, \{\varnothing, \{\varnothing\}\}\}",
                font_size=32
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        numbers.next_to(successor, DOWN, buff=0.8)

        self.play(FadeIn(numbers, shift=DOWN))
        self.wait(1)

        pattern = MathTex(
            r"n = \{0,1,2,\dots,n-1\}",
            font_size=38
        )
        pattern.next_to(numbers, DOWN, buff=0.8)

        self.play(Write(pattern))
        self.wait(2)
