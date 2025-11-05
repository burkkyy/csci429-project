from manim import *


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

        note = (
            Tex(
                r"\textit{Note: Definitions such as $G$, $S(T)$ (the set of predecessors of task $T$) "
                r"and $N(T)$ are introduced in Coffman \& Graham, ``Optimal Scheduling for Two-Processor Systems,'' ",
                tex_environment="flushleft",
            )
            .scale(0.6)
            .set_color(GRAY)
            .next_to(tfinal, DOWN, aligned_edge=LEFT)
        )

        algorithm_group = VGroup(tintro, ta, tb, tc, tfinal)

        self.play(Write(algorithm_group))
        self.play(FadeIn(note))
        self.wait(2)
