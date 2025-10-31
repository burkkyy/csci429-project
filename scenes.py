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


class AlgorithmA(Scene):
    def construct(self):
        tintro = (
            Tex(
                r"Let $r$ denote the number of tasks in $G$. "
                r"Algorithm $A$ assigns to each task $T$, an integer $\alpha(T) \in \{1, 2, \ldots, r\}$. "
                r"The map $\alpha$ is defined recursively as follows.",
                tex_environment="flushleft",
            )
            .scale(0.7)
            .to_edge(UP)
        )

        ta = (
            Tex(
                r"(a) An arbitrary task $T_0$ with $S(T) = \emptyset$ is chosen and $\alpha (T_0)$ is defined to be 1.",
                tex_environment="flushleft",
            )
            .scale(0.7)
            .next_to(tintro, DOWN, aligned_edge=LEFT)
        )

        tb = (
            Tex(
                r"(b) Suppose for some $k \leq r$, the integers $1, 2, ..., k-1$ have been assigned. "
                r"For each task $T$ for which $\alpha$ has been defined on all elements of $S(T)$, let $N(T)$ "
                r"denote the decreasing sequence of integers formed by ordering the set $\{\alpha (T'): T' \in S(T) \}$. "
                r"At least one of these tasks $T^*$ must satisfy $N(T^*) \leq N(T)$ for all "
                r"such tasks $T$. Choose one such $T^*$ and define $\alpha (T^*)$ to be $k$. ",
                tex_environment="flushleft",
            )
            .scale(0.7)
            .next_to(ta, DOWN, aligned_edge=LEFT)
        )

        tc = (
            Tex(
                r"(c) We repeat the assignment in (b) until all tasks of $G$ have been assigned some integer.",
                tex_environment="flushleft",
            )
            .scale(0.7)
            .next_to(tb, DOWN, aligned_edge=LEFT)
        )

        tfinal = (
            Tex(
                r"Finally, the list $L^*$ is defined by Algorithm $A$ to be $(U_r, U_{r-1}, ..., U_1)$ where $\alpha (U_k) = k, 1 \leq k \leq r$.",
                tex_environment="flushleft",
            )
            .scale(0.7)
            .next_to(tc, DOWN, aligned_edge=LEFT)
        )

        self.play(Write(tintro))
        self.wait(1)
        self.play(Write(ta))
        self.wait(1)
        self.play(Write(tb))
        self.wait(2)
        self.play(Write(tc))
        self.wait(2)
        self.play(Write(tfinal))
