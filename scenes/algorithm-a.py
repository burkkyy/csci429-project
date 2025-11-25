from manim import *


class PaperDisplay(Scene):
    def construct(self):
        # Load image (e.g. first page of paper)
        paper_img = ImageMobject("resources/paper-image-1.png")

        # Add white rectangle border
        border = SurroundingRectangle(paper_img, color=WHITE, buff=0.1, stroke_width=3)

        # Group image and border together
        paper_group = Group(paper_img, border).shift(LEFT * 4)

        # Create text elements
        title = Text("Optimal Scheduling for Two-Processor\nSystems", font_size=28)
        authors = Text("E. G. Coffman Jr and R. L. Graham", font_size=20, slant=ITALIC)
        text_group = VGroup(title, authors).arrange(DOWN, aligned_edge=LEFT)

        # Position text to the right of the image
        text_group.next_to(paper_group, RIGHT, buff=1.0)

        # Add everything to the scene
        self.add(paper_group, text_group)

        # Optional animation
        self.play(FadeIn(paper_group), FadeIn(text_group, shift=RIGHT))
        self.wait(5)

        new_img1 = ImageMobject("resources/paper-image-2.png").scale(1)
        new_border1 = SurroundingRectangle(
            new_img1, color=WHITE, buff=0.1, stroke_width=3
        )
        new_group1 = Group(new_img1, new_border1).move_to(paper_group.get_center())

        # Smooth transition
        self.play(FadeOut(paper_group), FadeIn(new_group1))
        self.wait(5)

        new_img2 = ImageMobject("resources/paper-image-3.png").scale(1)
        new_border2 = SurroundingRectangle(
            new_img2, color=WHITE, buff=0.1, stroke_width=3
        )
        new_group2 = Group(new_img2, new_border2).move_to(new_group1.get_center())

        # Smooth transition
        self.play(FadeOut(new_group1), FadeIn(new_group2))
        self.wait(5)


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


class OptimalScheduleForIntroDAG(Scene):
    def draw_arrow(self, parent_box, child_box, color=WHITE, buff=0.1):
        start = parent_box.get_bottom()
        end = child_box.get_top()

        arrow = Arrow(
            start=start,
            end=end,
            buff=buff,
            color=color,
            tip_shape=StealthTip,
            tip_length=0.2,
            stroke_width=3,
        )
        return arrow

    def create_processor(self, task, color=BLUE):
        task_worker = Arrow(
            start=task.get_left() + LEFT,
            end=task.get_left() + LEFT * 0.25,
            buff=0,
            color=color,
        )
        return task_worker

    def construct(self):
        tasks = []
        for i in range(8):
            label = MathTex(f"T_{{{i+1}}}", font_size=40)
            tasks.append(label)

        tasks[0].move_to(LEFT * 2.5 + UP * 3)
        tasks[1].move_to(LEFT * 4 + UP)
        tasks[2].move_to(LEFT + UP)
        tasks[3].move_to(LEFT * 4 + DOWN * 2 + UP)
        tasks[4].move_to(UP * 3)
        tasks[5].move_to(RIGHT * 3 + UP)
        tasks[6].move_to(LEFT + DOWN)
        tasks[7].move_to(RIGHT * 3 + UP * 3)

        arrows = []
        arrows.append(self.draw_arrow(tasks[0], tasks[1]))
        arrows.append(self.draw_arrow(tasks[0], tasks[2]))
        arrows.append(self.draw_arrow(tasks[2], tasks[3]))
        arrows.append(self.draw_arrow(tasks[2], tasks[6]))
        arrows.append(self.draw_arrow(tasks[4], tasks[2]))
        arrows.append(self.draw_arrow(tasks[5], tasks[6]))
        arrows.append(self.draw_arrow(tasks[7], tasks[5]))

        self.play(
            *[Create(task) for task in tasks], *[Create(arrow) for arrow in arrows]
        )

        status_box = Rectangle(
            width=config.frame_width - 1,
            height=1.5,
            color=WHITE,
            stroke_width=3,
        )

        status_box.to_edge(DOWN, buff=0.5)

        p1_label = Tex(r"$P_1$: $\emptyset$", font_size=32, color=BLUE)
        p2_label = Tex(r"$P_2$: $\emptyset$", font_size=32, color=RED)
        mu_label = MathTex(r"\mu = 0", font_size=32)
        l_label = MathTex(r"L = ()", font_size=32)

        left_group = VGroup(p1_label, p2_label).arrange(
            DOWN, aligned_edge=LEFT, buff=0.2
        )

        left_group.move_to(status_box.get_left() + RIGHT)

        right_group = VGroup(mu_label, l_label).arrange(
            DOWN, aligned_edge=LEFT, buff=0.2
        )

        right_group.move_to(status_box.get_right() + LEFT * 8)

        # Add to scene
        self.play(FadeIn(status_box))
        self.play(Write(left_group), Write(right_group))
        self.wait(2)

        # do optimal schedule
        time_step = 0

        def relabel_time_step(new_time):
            new_mu_label = MathTex(rf"\mu = {new_time}", font_size=32)
            new_mu_label.move_to(mu_label)
            mu_label.become(new_mu_label)

        def relabel_processors(p1=r"\emptyset", p2=r"\emptyset"):
            new_p1_label = Tex(rf"$P_1$: ${p1}$", font_size=32, color=BLUE)
            new_p2_label = Tex(rf"$P_2$: ${p2}$", font_size=32, color=RED)

            new_p1_label.next_to(p1_label, direction=LEFT, buff=0).align_to(
                p1_label, LEFT
            )
            new_p2_label.next_to(p2_label, direction=LEFT, buff=0).align_to(
                p2_label, LEFT
            )

            p1_label.become(new_p1_label)
            p2_label.become(new_p2_label)

        def relabel_schedule(schedule):
            new_l_label = MathTex(rf"L = ({schedule})", font_size=32)
            new_l_label.next_to(l_label, direction=LEFT, buff=0).align_to(l_label, LEFT)
            l_label.become(new_l_label)

        # Time step 0: Start p1 and p2 on T1 and T5
        p1 = self.create_processor(tasks[0], BLUE)
        p2 = self.create_processor(tasks[4], RED)
        TIME_STEP_DURATION = 1

        self.play(Create(p1), Create(p2))
        relabel_processors(r"T_1", r"T_5")
        self.wait(TIME_STEP_DURATION)

        schedule = r""

        # Time step 1
        self.play(
            FadeOut(tasks[0]),
            FadeOut(tasks[4]),
            FadeOut(arrows[0]),
            FadeOut(arrows[1]),
            FadeOut(arrows[4]),
        )
        self.play(
            p1.animate.move_to(
                tasks[2].get_left() + LEFT * 0.5,
            ),
            p2.animate.move_to(
                tasks[7].get_left() + LEFT * 0.5,
            ),
        )
        time_step += 1
        schedule += r"T_1, T_5"
        relabel_schedule(schedule)
        relabel_time_step(time_step)
        relabel_processors(r"T_3", r"T_8")
        self.wait(TIME_STEP_DURATION)

        # Time step 2
        self.play(
            FadeOut(tasks[2]),
            FadeOut(tasks[7]),
            FadeOut(arrows[2]),
            FadeOut(arrows[3]),
            FadeOut(arrows[6]),
        )
        self.play(
            p1.animate.move_to(
                tasks[1].get_left() + LEFT * 0.5,
            ),
            p2.animate.move_to(
                tasks[5].get_left() + LEFT * 0.5,
            ),
        )
        time_step += 1
        schedule += r", T_3, T_8"
        relabel_schedule(schedule)
        relabel_time_step(time_step)
        relabel_processors(r"T_2", r"T_6")
        self.wait(TIME_STEP_DURATION)

        # Time step 3
        self.play(
            FadeOut(tasks[1]),
            FadeOut(tasks[5]),
            FadeOut(arrows[5]),
        )
        self.play(
            p1.animate.move_to(
                tasks[3].get_left() + LEFT * 0.5,
            ),
            p2.animate.move_to(
                tasks[6].get_left() + LEFT * 0.5,
            ),
        )
        time_step += 1
        schedule += r", T_2, T_6"
        relabel_schedule(schedule)
        relabel_time_step(time_step)
        relabel_processors(r"T_4", r"T_7")
        self.wait(TIME_STEP_DURATION)

        # Time step 4
        self.play(
            FadeOut(tasks[3]),
            FadeOut(tasks[6]),
        )
        self.play(FadeOut(p1), FadeOut(p2))
        time_step += 1
        schedule += r", T_4, T_7"
        relabel_schedule(schedule)
        relabel_time_step(time_step)
        relabel_processors()
        self.wait(TIME_STEP_DURATION)

        # Fade out and show results
        fade_group = VGroup(
            status_box,
            p1_label,
            p2_label,
        )

        # Target positions
        final_l_label = l_label.copy().move_to(ORIGIN + DOWN * 0.5)
        final_mu_label = mu_label.copy().move_to(ORIGIN + UP * 0.5)

        self.play(
            FadeOut(fade_group),
            l_label.animate.move_to(final_l_label),
            mu_label.animate.move_to(final_mu_label),
            run_time=2,
        )

        # Optionally, enlarge and center the final labels for emphasis
        self.play(
            l_label.animate.scale(1.3),
            mu_label.animate.scale(1.3),
        )

        self.wait(2)

        comment1 = Tex(
            r"Our previous time was $5$, so we did one time step better",
            font_size=36,
        )

        comment = (
            VGroup(comment1).arrange(DOWN, buff=0.2).next_to(l_label, DOWN, buff=0.4)
        )

        self.play(FadeIn(comment))

        self.wait(2)


class CoffmanGrahamAlgorithmExplainerPart1(Scene):
    def draw_arrow(self, parent_box, child_box, color=WHITE, buff=0.1):
        start = parent_box.get_bottom()
        end = child_box.get_top()

        arrow = Arrow(
            start=start,
            end=end,
            buff=buff,
            color=color,
            tip_shape=StealthTip,
            tip_length=0.2,
            stroke_width=3,
        )
        return arrow

    def create_processor(self, task, color=BLUE):
        task_worker = Arrow(
            start=task.get_left() + LEFT,
            end=task.get_left() + LEFT * 0.25,
            buff=0,
            color=color,
        )
        return task_worker

    def construct(self):
        tasks = []
        for i in range(8):
            label = MathTex(f"T_{{{i+1}}}", font_size=40)
            tasks.append(label)

        tasks[0].move_to(LEFT * 2.5 + UP * 3)
        tasks[1].move_to(LEFT * 4 + UP)
        tasks[2].move_to(LEFT + UP)
        tasks[3].move_to(LEFT * 4 + DOWN * 2 + UP)
        tasks[4].move_to(UP * 3)
        tasks[5].move_to(RIGHT * 3 + UP)
        tasks[6].move_to(LEFT + DOWN)
        tasks[7].move_to(RIGHT * 3 + UP * 3)

        arrows = []
        arrows.append(self.draw_arrow(tasks[0], tasks[1]))
        arrows.append(self.draw_arrow(tasks[0], tasks[2]))
        arrows.append(self.draw_arrow(tasks[2], tasks[3]))
        arrows.append(self.draw_arrow(tasks[2], tasks[6]))
        arrows.append(self.draw_arrow(tasks[4], tasks[2]))
        arrows.append(self.draw_arrow(tasks[5], tasks[6]))
        arrows.append(self.draw_arrow(tasks[7], tasks[5]))

        self.add(*tasks)
        self.add(*arrows)

        status_box = Rectangle(
            width=config.frame_width - 1,
            height=1.5,
            color=WHITE,
            stroke_width=3,
        )

        status_box.to_edge(DOWN, buff=0.5)

        lstar_label = MathTex(r"L^* = ()", font_size=32)

        def rewrite_lstar(txt):
            new_lstar_label = MathTex(txt, font_size=32)
            new_lstar_label.next_to(lstar_label, direction=LEFT, buff=0).align_to(
                lstar_label, LEFT
            )

            self.play(Transform(lstar_label, new_lstar_label))

        lstar_label.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        lstar_label.move_to(status_box.get_right() + LEFT * 7)

        # Add to scene
        self.add(status_box)
        self.wait(2)

        self.play(Write(lstar_label))
        self.wait(2)

        rewrite_lstar(r"L^* = (\Box, \Box, \Box, \Box, \Box, \Box, \Box, \Box)")
        self.wait(2)

        definition_text1 = Text(
            "Successor of a task T: any task that depends on T",
            font_size=28,
            t2c={"Successor": BLUE},  # optional: color the word 'Successor'
        )
        definition_text2 = Text(
            "(i.e. tasks that can't be done until T is done).",
            font_size=28,
        )

        definition_text = VGroup(definition_text1, definition_text2).arrange(DOWN)

        # Create black background rectangle, slightly bigger than text
        definition_box = SurroundingRectangle(
            definition_text,
            color=WHITE,  # border color
            fill_color=BLACK,  # background color
            fill_opacity=1.0,
            buff=0.5,
            stroke_width=2,
        )

        # Group text and rectangle
        successor_group = VGroup(definition_box, definition_text)

        # Center on screen
        successor_group.move_to(ORIGIN)

        # Animate it
        self.play(FadeIn(successor_group))
        self.wait(3)

        self.play(FadeOut(successor_group))
        self.wait(2)

        self.play(
            Indicate(tasks[0], color=YELLOW, scale_factor=1.2),
            Indicate(tasks[4], color=YELLOW, scale_factor=1.2),
        )
        self.wait(1)

        self.play(
            Indicate(tasks[0], color=YELLOW, scale_factor=1.2),
            Indicate(tasks[7], color=YELLOW, scale_factor=1.2),
        )
        self.wait(1)

        self.play(
            Indicate(tasks[7], color=YELLOW, scale_factor=1.2),
            Indicate(tasks[4], color=YELLOW, scale_factor=1.2),
        )
        self.wait(1)

        self.wait(2)

        self.play(
            Indicate(tasks[1], color=YELLOW, scale_factor=1.2),
            Indicate(tasks[3], color=YELLOW, scale_factor=1.2),
            Indicate(tasks[6], color=YELLOW, scale_factor=1.2),
        )
        self.wait(2)

        rewrite_lstar(r"L^* = (\Box, \Box, \Box, \Box, \Box, T_2, T_4, T_7)")
        self.wait(2)

        t2_index_label = MathTex(f"T_2: 5", font_size=40)
        t4_index_label = MathTex(f"T_4: 6", font_size=40)
        t7_index_label = MathTex(f"T_7: 7", font_size=40)

        t2_index_label.next_to(tasks[1], direction=LEFT, buff=0).align_to(
            tasks[1], LEFT
        )
        t4_index_label.next_to(tasks[3], direction=LEFT, buff=0).align_to(
            tasks[3], LEFT
        )
        t7_index_label.next_to(tasks[6], direction=LEFT, buff=0).align_to(
            tasks[6], LEFT
        )

        self.play(
            Transform(tasks[1], t2_index_label),
            Transform(tasks[3], t4_index_label),
            Transform(tasks[6], t7_index_label),
        )
        self.wait(2)

        arrow_x = lstar_label.get_center()[0] + 0.5
        arrow_y = status_box.get_top()[1] - 0.6

        task_arrow = Arrow(
            start=[arrow_x, arrow_y + 0.5, 0],
            end=[arrow_x, arrow_y + 0.1, 0],
            color=YELLOW,
            stroke_width=15,
            buff=0,
        )

        self.bring_to_front(task_arrow)
        self.play(Create(task_arrow))
        self.wait(2)

        canidate_tasks = MathTex(
            r"\text{candidates} = \left[\begin{array}{l} T_3 \\ T_6 \end{array}\right]",
            font_size=32,
        )
        canidate_tasks.move_to(status_box.get_left() + RIGHT * 2.5)

        def rewrite_canidate_tasks(txt):
            if txt == "":
                self.play(FadeOut(canidate_tasks))

            new_canidate_tasks = MathTex(txt, font_size=32)
            new_canidate_tasks.next_to(canidate_tasks, direction=LEFT, buff=0).align_to(
                canidate_tasks, LEFT
            )
            self.play(Transform(canidate_tasks, new_canidate_tasks))

        self.play(Write(canidate_tasks))
        self.wait(2)

        self.play(Indicate(canidate_tasks))
        self.wait(2)

        canidate_tasks_expanded = MathTex(
            r"\text{candidates} = \left[\begin{array}{l} T_3: [7, 6] \\ T_6: [7] \end{array}\right]",
            font_size=32,
        )
        canidate_tasks_expanded.move_to(status_box.get_left() + RIGHT * 2.5)

        self.play(Transform(canidate_tasks, canidate_tasks_expanded))
        self.wait(2)

        definition_text = VGroup(
            Text("Lexicographical Ordering", font_size=28, color=BLUE),
            Tex(r"Given two arrays $A$ and $B$, $A < B$ if:", font_size=28),
            Tex(
                r"First differing elements at index $i$, $A[i] < B[i]$",
                font_size=28,
            ),
            Tex(
                r"OR",
                font_size=28,
            ),
            Tex(
                r"$A$ is a prefix of $B$",
                font_size=28,
            ),
        ).arrange(DOWN)

        definition_box = SurroundingRectangle(
            definition_text,
            color=WHITE,  # border color
            fill_color=BLACK,  # background color
            fill_opacity=1.0,
            buff=0.5,
            stroke_width=2,
        )

        definition = VGroup(definition_box, definition_text)

        self.play(FadeIn(definition))
        self.wait(3)
        self.play(FadeOut(definition))
        self.wait(3)

        def coffman_graham_step(
            txt1, new_canidate_tasks_txt, task_index, new_task_label_text, is_last=False
        ):
            new_lstar_label = MathTex(txt1, font_size=32)
            new_lstar_label.next_to(lstar_label, direction=LEFT, buff=0).align_to(
                lstar_label, LEFT
            )

            new_canidate_tasks = MathTex(
                r"\text{candidates} = \left[\begin{array}{l} \\ \end{array}\right]",
                font_size=32,
            )
            new_canidate_tasks.next_to(canidate_tasks, direction=LEFT, buff=0).align_to(
                canidate_tasks, LEFT
            )

            task_index_label = MathTex(new_task_label_text, font_size=40)

            task_index_label.next_to(
                tasks[task_index], direction=LEFT, buff=0
            ).align_to(tasks[task_index], LEFT)

            animations = [
                Transform(lstar_label, new_lstar_label),
            ]

            if not is_last:
                animations.append(task_arrow.animate.shift(LEFT * 0.4))

            animations.append(
                Transform(tasks[task_index], task_index_label),
            )

            animations.append(
                Transform(canidate_tasks, new_canidate_tasks),
            )

            self.play(*animations)

            self.wait(1)

            if is_last:
                self.play(FadeOut(canidate_tasks), FadeOut(task_arrow))
            else:
                rewrite_canidate_tasks(new_canidate_tasks_txt)

        coffman_graham_step(
            r"L^* = (\Box, \Box, \Box, \Box, T_6, T_2, T_4, T_7)",
            r"\text{candidates} = \left[\begin{array}{l} T_3: [7, 6] \\ T_8: [4] \end{array}\right]",
            5,
            r"T_6: 4",
        )
        self.wait(1)

        # 1. write canidates
        # 2. wait(1)
        # 3. coffman graham step + write task

        coffman_graham_step(
            r"L^* = (\Box, \Box, \Box, T_8, T_6, T_2, T_4, T_7)",
            r"\text{candidates} = \left[\begin{array}{l} T_3: [7, 6] \\ \end{array}\right]",
            7,
            r"T_8: 3",
        )
        self.wait(1)

        coffman_graham_step(
            r"L^* = (\Box, \Box, T_3, T_8, T_6, T_2, T_4, T_7)",
            r"\text{candidates} = \left[\begin{array}{l} T_1: [5, 2] \\ T_5: [2] \end{array}\right]",
            2,
            r"T_3: 2",
        )
        self.wait(1)

        coffman_graham_step(
            r"L^* = (\Box, T_5, T_3, T_8, T_6, T_2, T_4, T_7)",
            r"\text{candidates} = \left[\begin{array}{l} T_1: [5, 2] \end{array}\right]",
            4,
            r"T_5: 1",
        )
        self.wait(1)

        coffman_graham_step(
            r"L^* = (T_1, T_5, T_3, T_8, T_6, T_2, T_4, T_7)", r"", 0, r"T_1: 0", True
        )
        self.wait(2)


class CoffmanGrahamAlgorithmRecap(Scene):
    def construct(self):
        title = Text("Coffman-Graham Algorithm Recap", font_size=32)
        title.to_edge(UP)

        self.play(Write(title))
        self.wait(2)

        body = Tex(
            r"Let $G$ be a task graph and $L^*$ be an array of size equal to the number of tasks in $G$.",
            font_size=30,
            tex_environment="flushleft",
        )

        first_step = Tex(
            r"1. Put all tasks with no successors at the back of $L^*$ in any order.",
            font_size=30,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        point_intro = Tex(
            r"2. While $L^*$ is not fully filled in, do the following:",
            font_size=30,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        point1 = Tex(
            r"i. Consider all tasks whose successors have\\",
            r"indices defined in $L^*$ and make it a candidate.\\",
            r"But don't make a task a candidate if it's already in $L^*$",
            font_size=30,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        point2 = Tex(
            r"ii. For each candidate task, make an array with\\",
            r"each element being its successor indices in $L^*$\\",
            r"sorted in decreasing order",
            font_size=30,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        point3 = Tex(
            r"iii. Pick the candidate task with the\\",
            r"lexicographically smallest array",
            font_size=30,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        point_finish = Tex(
            r"$L^*$ is the optimal schedule for the task graph",
            font_size=30,
        )

        body.shift(UP * 2.5)

        first_step.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        first_step.next_to(body, DOWN, buff=0.7)
        first_step.align_to(body, LEFT)
        first_step.shift(UP * 0.5 + RIGHT)

        second_step = VGroup(point_intro, point1, point2, point3, point_finish)
        second_step.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        second_step.next_to(first_step, DOWN, buff=0.7)
        second_step.align_to(first_step, LEFT)
        second_step.shift(UP * 0.5)

        point1.shift(RIGHT * 0.5)
        point2.shift(RIGHT * 0.5)
        point3.shift(RIGHT * 0.5)

        self.play(Write(body), Write(first_step))
        self.wait(2)

        self.play(Write(second_step))
        self.wait(2)

        self.play(Write(point_finish))
        self.wait(3)


class CoffmanGrahamAlgorithmCodeAndAnalysisSetup(Scene):
    def construct(self):
        task_graph_code = Code(
            code_string="""
class TaskGraph:
    def add_task():
        ...

    def add_successor():
        ...

    def number_of_tasks():
        ...

    def successors(task):
        ...
""",
            tab_width=4,
            background="rectangle",
            language="Python",
        ).scale(0.8)

        self.play(FadeIn(task_graph_code))
        self.wait(4)
        self.play(FadeOut(task_graph_code))

        helper_functions_code1 = Code(
            code_string="""
def less_than_lexicographically(a, b):
    if len(a) == 0 and len(b) == 0:
        return False
    if len(a) == 0:
        return True

    for i in range(min(len(a), len(b))):
        if a[i] < b[i]:
            return True
        elif a[i] > b[i]:
            return False

    return len(a) < len(b)
""",
            tab_width=4,
            background="rectangle",
            language="Python",
        ).scale(0.8)

        self.play(FadeIn(helper_functions_code1))
        self.wait(4)
        self.play(FadeOut(helper_functions_code1))

        helper_functions_code2 = Code(
            code_string="""
def smallest_lexicographical_array(N):
    current_min_n = None
    for n in N:
        if current_min_n == None:
            current_min_n = n
            continue

        lt_eq_lex = less_than_lexicographically(N[n], N[current_min_n])

        if lt_eq_lex:
            current_min_n = n
        elif N[n] == N[current_min_n]:
            if n < current_min_n:
                current_min_n = n

    return current_min_n
""",
            tab_width=4,
            background="rectangle",
            language="Python",
        ).scale(0.8)

        self.play(FadeIn(helper_functions_code2))
        self.wait(4)


class CoffmanGrahamAlgorithmCodeAndAnalysis(Scene):
    def construct(self):
        algorithm_a_code_part1 = Code(
            code_string="""
def coffman_graham_algorithm(G: TaskGraph):
    r = G.number_of_tasks()
    k = 1
    alpha = {}

    for T in G.tasks():
        if not G.successors(T):
            alpha[T] = k
            k += 1
""",
            tab_width=4,
            background="rectangle",
            language="Python",
        ).scale(0.8)

        self.play(FadeIn(algorithm_a_code_part1))
        self.wait(4)
        self.play(FadeOut(algorithm_a_code_part1))

        algorithm_a_code_part2 = Code(
            code_string="""
def coffman_graham_algorithm(G: TaskGraph):
    r = G.number_of_tasks()
    k = 1
    alpha = {}

    for T in G.tasks():
        ...

    while k <= r:
        N = {}
        for T in G.tasks():
            if T in alpha:
                continue

            all_successors_defined = True
            S_T = G.successors(T)

            for t in S_T:
                if t not in alpha:
                    all_successors_defined = False
                    break

            if all_successors_defined:
                N[T] = sorted([alpha[t] for t in S_T], reverse=True)
""",
            tab_width=4,
            background="rectangle",
            language="Python",
        ).scale(0.8)

        self.play(FadeIn(algorithm_a_code_part2))
        self.wait(4)
        self.play(FadeOut(algorithm_a_code_part2))

        algorithm_a_code_part3 = Code(
            code_string="""
def coffman_graham_algorithm(G: TaskGraph):
    r = G.number_of_tasks()
    k = 1
    alpha = {}

    for T in G.tasks():
        ... 

    while k <= r:
        N = {}
        for T in G.tasks():
            ...

            for t in S_T:
                ...
            
            ...

        current_min_n = smallest_lexicographical_array(N)
        alpha[current_min_n] = k
        k += 1
    
    schedule = sorted(alpha.keys(), key=lambda task: alpha[task])
    return schedule[::-1]
""",
            tab_width=4,
            background="rectangle",
            language="Python",
        ).scale(0.8)

        self.play(FadeIn(algorithm_a_code_part3))
        self.wait(4)

        algorithm_a_code_part4 = Code(
            code_string="""
def coffman_graham_algorithm(G: TaskGraph):
    r = G.number_of_tasks()
    k = 1
    alpha = {}

    for T in G.tasks():
        ... 

    while k <= r:  # O(n)
        N = {}
        for T in G.tasks():  # O(n)
            ...

            for t in S_T:  # O(n)
                ...
            
            ...

        current_min_n = smallest_lexicographical_array(N)
        alpha[current_min_n] = k
        k += 1
    
    schedule = sorted(alpha.keys(), key=lambda task: alpha[task])
    return schedule[::-1]
""",
            tab_width=4,
            background="rectangle",
            language="Python",
        ).scale(0.8)

        self.play(FadeIn(algorithm_a_code_part4))
        self.wait(4)

        big_o_text = Tex(r"Time complexity:\\$O(n^3)$")
        self.bring_to_front(big_o_text)
        big_o_text.shift(RIGHT * 3)
        self.play(FadeIn(big_o_text))
