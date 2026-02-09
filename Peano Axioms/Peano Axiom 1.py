from manim import *

class PeanoAxiom1(Scene):
    def construct(self):
        title = Text("Peano Axiom 1(Existance)", font_size=48)
        title.to_edge(UP)

        axiom = MathTex(
            r"\exists \, 0 \in \mathbb{N}",
            font_size=72
        )

        explanation = Text(
            "0(Zero) is a natural number",
            font_size=32
        )
        explanation.next_to(axiom, DOWN, buff=0.6)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(axiom))
        self.wait(0.5)
        self.play(FadeIn(explanation))
        self.wait(2)
