from manim import *

class PeanoAxiom2(Scene):
    def construct(self):
        title = Text("Peano Axiom 2", font_size=48)
        title.to_edge(UP)

        axiom = MathTex(
            r"\forall n \in \mathbb{N}, \; S(n) \in \mathbb{N}",
            font_size=64
        )

        explanation = Text(
            "Every natural number has a unique successor",
            font_size=32
        )
        explanation.next_to(axiom, DOWN, buff=0.6)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(axiom))
        self.wait(0.5)
        self.play(FadeIn(explanation))
        self.wait(2)
