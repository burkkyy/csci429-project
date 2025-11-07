from manim import *


TASK_WIDTH = 3
TASK_HEIGHT = 0.8


class Title(Scene):
    def construct(self):
        title = Text(
            "Visual Intuition for the Optimal Scheduling of M-Processor Systems",
            font_size=26,
        )

        VGroup(title).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(FadeIn(title))
        self.wait(4)

        self.play(FadeOut(title))


class TaskIntroduction(Scene):
    def construct(self):
        tasks = [
            "Buy Groceries",
            "Cook Dinner",
            "Clean Up",
            "Do Laundry",
            "Put Away Laundry",
        ]

        # Step 1: create bullet points
        bullet_points = []
        labels = []
        bullet_label_pairs = []
        for text in tasks:
            bullet = Text("•", font_size=60, color=WHITE)
            label = Text(text, font_size=40)
            bullet_points.append(bullet)
            labels.append(label)

            pair = VGroup(bullet, label).arrange(
                RIGHT, buff=0.4
            )  # bullet next to label
            bullet_label_pairs.append(pair)

        group = VGroup(*bullet_label_pairs).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        group.move_to(ORIGIN)

        self.play(LaggedStart(*[Write(pair) for pair in group], lag_ratio=0.2))
        self.wait(2)

        self.play(
            *[FadeOut(bullet_point) for bullet_point in bullet_points],
        )
        self.wait(2)

        # Move boxs around
        self.play(
            # Buy Groceries box
            labels[0].animate.move_to(UP * 2 + LEFT * 3),
            # cook_dinner_box
            labels[1].animate.move_to(LEFT * 3),
            # clean_up_box
            labels[2].animate.move_to(DOWN * 2 + LEFT * 3),
            # do_laundry_box
            labels[3].animate.move_to(RIGHT * 2 + UP * 2),
            # put_away_laundry_box
            labels[4].animate.move_to(RIGHT * 2),
        )
        self.wait(2)

        # Draw arrows
        a1 = Arrow(
            start=labels[0].get_bottom(),
            end=labels[1].get_top(),
            buff=0.1,
        )
        a2 = Arrow(
            start=labels[1].get_bottom(),
            end=labels[2].get_top(),
            buff=0.1,
        )
        a3 = Arrow(
            start=labels[3].get_bottom(),
            end=labels[4].get_top(),
            buff=0.1,
        )
        self.play(Create(a1), Create(a2), Create(a3))
        self.wait(2)

        # Animate working on tasks using naive method
        task_worker = Arrow(
            start=labels[0].get_left() + LEFT * 1.5,
            end=labels[0].get_left() + LEFT * 0.5,
            buff=0,
            color=BLUE,
        )

        self.play(GrowArrow(task_worker))
        self.wait(1)
        self.play(FadeOut(labels[0]), FadeOut(a1))

        self.play(
            task_worker.animate.move_to(
                labels[1].get_left() + LEFT,
            )
        )
        self.wait(1)

        self.play(FadeOut(labels[1]), FadeOut(a2))
        self.play(
            task_worker.animate.move_to(
                labels[2].get_left() + LEFT,
            )
        )
        self.wait(1)

        self.play(FadeOut(labels[2]))
        self.play(
            task_worker.animate.move_to(
                labels[3].get_left() + LEFT,
            )
        )
        self.wait(1)

        self.play(FadeOut(labels[3]), FadeOut(a3))
        self.play(
            task_worker.animate.move_to(
                labels[4].get_left() + LEFT,
            )
        )
        self.wait(1)

        self.play(FadeOut(labels[4]))
        self.wait(1)


class TimeComplexityExplanation(Scene):
    def construct(self):
        title = Text("Naive Task Scheduling Approach", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Pseudocode text
        code = (
            Code(
                code_string="""
tasks = {...}
schedule = []

for i in range(len(tasks)):
    for task in tasks:
        if task has no dependencies:
            schedule.append(task)
            tasks.remove(task)
            break
""",
                tab_width=4,
                background="rectangle",
                language="Python",
            )
            .scale(0.8)
            .to_edge(LEFT)
        )

        self.play(FadeIn(code, shift=RIGHT))
        self.wait(2)

        # Complexity explanation text
        comment = (
            Tex(
                r"Time complexity of this approach: \\$O(n^2)$",
            )
            .scale(0.8)
            .next_to(code, buff=0.8)
        )
        comment.next_to(code, RIGHT)

        # Fade in the complexity line
        self.play(FadeIn(comment))
        self.wait(2)


class DAGScene(Scene):
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

    def create_task_worker(self, task, color=BLUE):
        task_worker = Arrow(
            start=task.get_left() + LEFT,
            end=task.get_left() + LEFT * 0.25,
            buff=0,
            color=color,
        )
        return task_worker

    def construct(self):
        tasks = [
            "Task A",
            "Task B",
            "Task C",
            "Task D",
            "Task E",
            "Task F",
            "Task G",
            "Task H",
        ]

        boxes = []
        for task in tasks:
            label = Text(task, font_size=30)
            box = SurroundingRectangle(label, color=WHITE, stroke_width=3, buff=0.3)
            boxes.append(VGroup(box, label))

        # Special arrange boxes
        boxes[0].move_to(LEFT * 2.5 + UP * 2)
        boxes[1].move_to(LEFT * 4)
        boxes[2].move_to(LEFT)
        boxes[3].move_to(LEFT * 4 + DOWN * 2)
        boxes[4].move_to(UP * 2)
        boxes[5].move_to(RIGHT * 3)
        boxes[6].move_to(LEFT + DOWN * 2)
        boxes[7].move_to(RIGHT * 3 + UP * 2)

        arrows = []
        arrows.append(self.draw_arrow(boxes[0], boxes[1]))
        arrows.append(self.draw_arrow(boxes[0], boxes[2]))
        arrows.append(self.draw_arrow(boxes[2], boxes[3]))
        arrows.append(self.draw_arrow(boxes[2], boxes[6]))
        arrows.append(self.draw_arrow(boxes[4], boxes[2]))
        arrows.append(self.draw_arrow(boxes[5], boxes[6]))
        arrows.append(self.draw_arrow(boxes[7], boxes[5]))

        self.play(*[Create(box) for box in boxes], *[Create(arrow) for arrow in arrows])
        self.wait(2)

        # Relabel the boxes
        new_labels = []
        for i in range(len(boxes)):
            new_label = MathTex(f"T_{{{i+1}}}", font_size=40)
            new_label.move_to(boxes[i][1].get_center())  # Position at old label center
            new_labels.append(new_label)

        animations = []
        for i in range(len(boxes)):
            animations.append(FadeOut(boxes[i][0]))  # Fade out the box
            animations.append(Transform(boxes[i][1], new_labels[i]))  # Transform text

        self.play(*animations)
        self.wait(2)

        # Shift DAG up
        dag_group = VGroup(*[box[1] for box in boxes], *arrows)
        self.play(dag_group.animate.shift(UP))
        self.wait(2)

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
        self.play(Write(left_group))
        self.play(Write(right_group))
        self.wait(2)

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
        p1 = self.create_task_worker(new_labels[0], BLUE).shift(UP)
        p2 = self.create_task_worker(new_labels[4], RED).shift(UP)
        TIME_STEP_DURATION = 1

        self.play(Create(p1), Create(p2))
        relabel_processors(r"T_1", r"T_5")
        self.wait(TIME_STEP_DURATION)

        schedule = r""
        current_labels = [box[1] for box in boxes]
        arrow_group = dag_group[len(boxes) :]

        # Time step 1
        self.play(
            FadeOut(current_labels[0]),
            FadeOut(current_labels[4]),
            FadeOut(arrow_group[0]),
            FadeOut(arrow_group[1]),
            FadeOut(arrow_group[4]),
        )
        self.play(
            p1.animate.move_to(
                new_labels[1].get_left() + LEFT * 0.5 + UP,
            ),
            p2.animate.move_to(
                new_labels[2].get_left() + LEFT * 0.5 + UP,
            ),
        )
        time_step += 1
        schedule += r"T_1, T_5"
        relabel_schedule(schedule)
        relabel_time_step(time_step)
        relabel_processors(r"T_2", r"T_3")
        self.wait(TIME_STEP_DURATION)

        # Time step 2
        self.play(
            FadeOut(current_labels[1]),
            FadeOut(current_labels[2]),
            FadeOut(arrow_group[2]),
            FadeOut(arrow_group[3]),
        )
        self.play(
            p1.animate.move_to(
                new_labels[3].get_left() + LEFT * 0.5 + UP,
            ),
            p2.animate.move_to(
                new_labels[7].get_left() + LEFT * 0.5 + UP,
            ),
        )
        time_step += 1
        schedule += r", T_2, T_3"
        relabel_schedule(schedule)
        relabel_time_step(time_step)
        relabel_processors(r"T_4", r"T_8")
        self.wait(TIME_STEP_DURATION)

        # Time step 3
        self.play(
            FadeOut(current_labels[3]),
            FadeOut(current_labels[7]),
            FadeOut(arrow_group[6]),
        )
        self.play(
            p1.animate.move_to(
                new_labels[5].get_left() + LEFT * 0.5 + UP,
            ),
            FadeOut(p2),
        )
        time_step += 1
        schedule += r", T_4, T_8"
        relabel_schedule(schedule)
        relabel_time_step(time_step)
        relabel_processors(r"T_4")
        self.wait(TIME_STEP_DURATION)

        # Time step 4
        self.play(
            FadeOut(current_labels[5]),
            FadeOut(arrow_group[5]),
        )
        self.play(
            p1.animate.move_to(
                new_labels[6].get_left() + LEFT * 0.5 + UP,
            ),
        )
        time_step += 1
        schedule += r", T_6"
        relabel_schedule(schedule)
        relabel_time_step(time_step)
        relabel_processors(r"T_5")
        self.wait(TIME_STEP_DURATION)

        # Time step 5
        self.play(
            FadeOut(current_labels[6]),
        )
        self.play(FadeOut(p1))
        time_step += 1
        schedule += r", T_7"
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


class DAGSceneCounterExample(Scene):
    def construct(self):
        pass
