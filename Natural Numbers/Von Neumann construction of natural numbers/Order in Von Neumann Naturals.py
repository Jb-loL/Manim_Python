from manim import *

class VonNeumannOrder(Scene):
    def construct(self):

        title = Text("Order in von Neumann Naturals", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))

        nums = VGroup(
            MathTex(r"0 = \varnothing", font_size=34),
            MathTex(r"1 = \{0\}", font_size=34),
            MathTex(r"2 = \{0,1\}", font_size=34),
            MathTex(r"3 = \{0,1,2\}", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        nums.next_to(title, DOWN, buff=0.8)

        self.play(FadeIn(nums, shift=DOWN))
        self.wait(1)

        examples = VGroup(
            MathTex(r"0 \in 1", font_size=36),
            MathTex(r"1 \in 2", font_size=36),
            MathTex(r"2 \in 3", font_size=36),
        ).arrange(DOWN, buff=0.4)

        examples.next_to(nums, RIGHT, buff=1.5)

        self.play(Write(examples))
        self.wait(1)

        conclusion = MathTex(
            r"m < n \quad \Longleftrightarrow \quad m \in n",
            font_size=40
        )
        conclusion.next_to(nums, DOWN, buff=1)

        self.play(Write(conclusion))
        self.wait(2)