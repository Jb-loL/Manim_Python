from manim import *

class PeanoAxiom4(Scene):
    def construct(self):
        title = Text("Peano Axiom 4", font_size=48)
        title.to_edge(UP)

        axiom = MathTex(
            r"\forall m,n \in \mathbb{N}, \;"
            r"S(m) = S(n) \Rightarrow m = n",
            font_size=60
        )

        explanation = Text(
            "If two natural numbers have the same successor,\n"
            "then the numbers themselves must be equal.",
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
