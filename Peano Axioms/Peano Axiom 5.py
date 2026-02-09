from manim import *

class PeanoAxiom5(Scene):
    def construct(self):
        title = Text("Peano Axiom 5", font_size=46)
        title.to_edge(UP)

        axiom = MathTex(
            r"\Big( P(0)\;\wedge\;"
            r"\forall n \in \mathbb{N}\,[P(n)\Rightarrow P(S(n))] \Big)"
            r"\Rightarrow \forall n \in \mathbb{N}\, P(n)",
            font_size=48
        )

        explanation = Text(
            "If a set contains zero and the sucessor of every number\n"
            "then the set contains the natural numbers\n",
            font_size=28,
            line_spacing=1.2
        )
        explanation.next_to(axiom, DOWN, buff=0.6)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(axiom))
        self.wait(0.5)
        self.play(FadeIn(explanation))
        self.wait(2)
from manim import *

class PeanoAxiom5(Scene):
    def construct(self):
        title = Text("Peano Axiom 5", font_size=46)
        title.to_edge(UP)

        axiom = MathTex(
            r"\Big( P(0)\;\wedge\;"
            r"\forall n \in \mathbb{N}\,[P(n)\Rightarrow P(S(n))] \Big)"
            r"\Rightarrow \forall n \in \mathbb{N}\, P(n)",
            font_size=48
        )

        explanation = Text(
            "If a set contains zero and the sucessor of every number\n"
            "then the set contains the natural numbers\n",
            font_size=28,
            line_spacing=1.2
        )
        explanation.next_to(axiom, DOWN, buff=0.6)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(axiom))
        self.wait(0.5)
        self.play(FadeIn(explanation))
        self.wait(2)
