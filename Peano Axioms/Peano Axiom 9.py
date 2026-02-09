from manim import *

class PeanoAxiom9(Scene):
    def construct(self):

        title = Text("Peano Axiom 9 (Multiplication: Recursive Step)", font_size=44)
        title.to_edge(UP)
        self.play(Write(title))

        axiom = MathTex(
            r"\forall x,y \in \mathbb{N}, \quad x \cdot S(y) = (x \cdot y) + x",
            font_size=38
        )
        axiom.next_to(title, DOWN, buff=0.8)

        self.play(Write(axiom))
        self.wait(1)

        example = MathTex(
            r"3 \cdot 4 = (3 \cdot 3) + 3 = 12",
            font_size=36
        )
        example.next_to(axiom, DOWN, buff=0.6)

        self.play(Write(example))
        self.wait(1)

        explanation = Text(
            "In other words, to multiply x by y + 1,\n"
            "first multiply x by y, then add x.\n"
            "This defines multiplication as repeated addition.",
            font_size=30
        )
        explanation.next_to(example, DOWN, buff=0.6)

        self.play(FadeIn(explanation, shift=DOWN))
        self.wait(2)
