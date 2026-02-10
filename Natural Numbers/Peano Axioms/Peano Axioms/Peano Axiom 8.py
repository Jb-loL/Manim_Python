from manim import *

class PeanoAxiom8(Scene):
    def construct(self):

        title = Text("Peano Axiom 8 (Multiplication: Base Case)", font_size=44)
        title.to_edge(UP)
        self.play(Write(title))

        axiom = MathTex(
            r"\forall x \in \mathbb{N}, \quad x \cdot 0 = 0",
            font_size=40
        )
        axiom.next_to(title, DOWN, buff=0.8)

        self.play(Write(axiom))
        self.wait(1)

        example = MathTex(
            r"7 \cdot 0 = 0",
            font_size=36
        )
        example.next_to(axiom, DOWN, buff=0.6)

        self.play(Write(example))
        self.wait(1)

        explanation = Text(
            "In other words, multiplying any natural number by zero\n"
            "results in zero. This is the base case for defining\n"
            "multiplication.",
            font_size=30
        )
        explanation.next_to(example, DOWN, buff=0.6)

        self.play(FadeIn(explanation, shift=DOWN))
        self.wait(2)
