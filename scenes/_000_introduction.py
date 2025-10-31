from manim import *


class Introduction(Scene):
    def construct(self):
        title = Text("Optimal Scheduling for Two-Processor Systems", font_size=36)
        subtitle = Text(
            "E. G. Coffman, Jr. and R. L. Graham", font_size=20, slant=ITALIC
        )

        VGroup(title, subtitle).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)

        self.play(FadeOut(title, subtitle))

        table_of_contents = Text(r"a" r"b")

        self.play(FadeIn(table_of_contents))
