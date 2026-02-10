from manim import *

class PeanoAxiomMinimality(Scene):
    def construct(self):

        title = Text("Peano Axiom 5(Induction/Minimality) Example", font_size=44)
        title.to_edge(UP)
        self.play(Write(title))

        axiom = MathTex(
            r"\forall P \subseteq \mathbb{N},",
            r"\quad P(0)",
            r"\ \land\ ",
            r"\forall m \in \mathbb{N},\ (P(m) \Rightarrow P(S(m)))",
            r"\ \Rightarrow\ ",
            r"P = \mathbb{N}",
        )
        axiom.next_to(title, DOWN, buff=0.8)

        self.play(Write(axiom))
        self.wait(1)

        explanation = VGroup(
            Text("• 0 has the property P", font_size=28),
            Text("• If a number has P, its successor also has P", font_size=28),
            Text("• Then every natural number has P", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        explanation.next_to(axiom, DOWN, buff=0.7)

        self.play(FadeIn(explanation, shift=DOWN))
        self.wait(1)

        conclusion = Text(
            "In other words, the natural numbers are the smallest set\n"
            "satisfying these properties.",
            font_size=30,
        )
        conclusion.next_to(explanation, DOWN, buff=0.6)

        self.play(Write(conclusion))
        self.wait(2)
