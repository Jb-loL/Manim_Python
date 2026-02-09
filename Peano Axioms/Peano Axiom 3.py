from manim import *

class PeanoAxiom3(Scene):
    def construct(self):
        title = Text("Peano Axiom 3(Excluding loops)", font_size=48)
        title.to_edge(UP)

        axiom = MathTex(
            r"\forall n \in \mathbb{N}, \; S(n) \neq 0",
            font_size=64
        )

        explanation = Text(
            "Zero is not the successor of any natural number.\n"
            "In other words, zero is the first natural number and has no predecessor.",
            font_size=30,
            line_spacing=1.2
        )
        explanation.next_to(axiom, DOWN, buff=0.6)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(axiom))
        self.wait(0.5)
        self.play(FadeIn(explanation))
        self.wait(2)
