from manim import *

class PeanoAxiom7(Scene):
    def construct(self):

        title = Text("Peano Axiom 7 (Addition: Recursive Step)", font_size=44)
        title.to_edge(UP)
        self.play(Write(title))

        axiom = MathTex(
            r"\forall x,y \in \mathbb{N}, \quad x + S(y) = S(x + y)",
            font_size=40
        )
        axiom.next_to(title, DOWN, buff=0.8)

        self.play(Write(axiom))
        self.wait(1)

        example = MathTex(
            r"3 + 2 = S(3 + 1) = S(S(3 + 0)) = 5",
            font_size=34
        )
        example.next_to(axiom, DOWN, buff=0.6)

        self.play(Write(example))
        self.wait(1)

        explanation = Text(
            "In other words, to add x to y + 1,\n"
            "first add x to y, then take the successor.\n"
            "This defines addition recursively.",
            font_size=30
        )
        explanation.next_to(example, DOWN, buff=0.6)

        self.play(FadeIn(explanation, shift=DOWN))
        self.wait(2)
