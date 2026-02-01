from manim import *

class AreaOfCube3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        headline = Text("Surface Area of a Cube", font_size=42).to_edge(UP)
        self.add_fixed_in_frame_mobjects(headline)
        self.play(Write(headline))

        cube = Cube(side_length=2)
        cube.set_stroke(WHITE, 2)
        cube.set_fill(BLUE, opacity=0.15)

        self.play(Create(cube), run_time=2)

        faces = VGroup(*cube.submobjects)
        face = faces[0]

        vertices = face.get_vertices()

        edge1 = Line(vertices[0], vertices[1], color=YELLOW)
        edge2 = Line(vertices[1], vertices[2], color=YELLOW)
        edge3 = Line(vertices[2], vertices[3], color=YELLOW)

        label1 = MathTex("a").scale(0.8).move_to(edge1.get_center() + 0.2 * OUT)
        label2 = MathTex("a").scale(0.8).move_to(edge2.get_center() + 0.2 * OUT)
        label3 = MathTex("a").scale(0.8).move_to(edge3.get_center() + 0.2 * OUT)

        self.play(Create(edge1), Create(edge2), Create(edge3))
        self.play(Write(label1), Write(label2), Write(label3))

        colors = [RED, GREEN, ORANGE, PURPLE, TEAL, PINK]

        for face, color in zip(faces, colors):
            face.set_fill(color, opacity=0.55)
            self.play(FadeIn(face), run_time=0.4)

        self.play(
            Rotate(cube, angle=PI / 2, axis=UP),
            run_time=3
        )

        self.wait(2)
