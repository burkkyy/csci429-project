from manim import *
from collections import defaultdict


class JobGraphScheduling(Scene):
    def construct(self):
        # Title
        title = Text("Coffman-Graham Two-Processor Scheduling", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Define jobs and their positions
        jobs_data = {
            "J1": {"pos": LEFT * 3 + UP * 2},
            "J2": {"pos": LEFT * 3 + DOWN * 2},
            "J3": {"pos": ORIGIN + UP * 0.5},
            "J4": {"pos": ORIGIN + DOWN * 0.5},
            "J5": {"pos": RIGHT * 3 + UP * 0.5},
            "J6": {"pos": RIGHT * 3 + DOWN * 0.5},
        }

        # Precedence constraints
        edges = [
            ("J1", "J3"),
            ("J2", "J3"),
            ("J1", "J4"),
            ("J3", "J5"),
            ("J4", "J6"),
        ]

        # Create job nodes
        jobs = {}
        job_labels = {}

        for job_id, data in jobs_data.items():
            circle = Circle(radius=0.4, color=BLUE, fill_opacity=0.3)
            circle.move_to(data["pos"])
            label = Text(job_id, font_size=24)
            label.move_to(data["pos"])

            jobs[job_id] = circle
            job_labels[job_id] = label

        # Create edges
        arrows = []
        for src, dst in edges:
            arrow = Arrow(
                jobs[src].get_center(),
                jobs[dst].get_center(),
                buff=0.4,
                color=GRAY,
                stroke_width=3,
            )
            arrows.append(arrow)

        # Animate graph creation
        subtitle = Text("Job Precedence Graph (DAG)", font_size=24)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(0.3)

        # Draw all jobs
        self.play(
            *[Create(circle) for circle in jobs.values()],
            *[Write(label) for label in job_labels.values()],
            run_time=1.5,
        )
        self.wait(0.5)

        # Draw edges
        self.play(*[Create(arrow) for arrow in arrows], run_time=1.5)
        self.wait(1)

        # Build adjacency info for scheduling
        predecessors = defaultdict(list)
        for src, dst in edges:
            predecessors[dst].append(src)

        # Scheduling simulation
        completed = set()
        schedule = []
        time = 0

        all_jobs = list(jobs_data.keys())

        # Generate schedule
        while len(completed) < len(all_jobs):
            available = [
                job
                for job in all_jobs
                if job not in completed
                and all(pred in completed for pred in predecessors[job])
            ]

            if not available:
                break

            scheduled = sorted(available)[:2]  # 2 processors
            schedule.append({"time": time, "jobs": scheduled})

            for job in scheduled:
                completed.add(job)

            time += 1

        # Show scheduling process
        self.play(FadeOut(subtitle))

        schedule_title = Text("Two-Processor Schedule", font_size=28)
        schedule_title.next_to(title, DOWN)
        self.play(Write(schedule_title))
        self.wait(0.5)

        # Reset for animation
        completed = set()

        # Create processor boxes
        proc1_box = Rectangle(width=2.5, height=1, color=GREEN)
        proc1_box.to_edge(DOWN).shift(LEFT * 2.5 + UP * 0.3)
        proc1_label = Text("Processor 1", font_size=20)
        proc1_label.next_to(proc1_box, UP, buff=0.2)

        proc2_box = Rectangle(width=2.5, height=1, color=GREEN)
        proc2_box.to_edge(DOWN).shift(RIGHT * 2.5 + UP * 0.3)
        proc2_label = Text("Processor 2", font_size=20)
        proc2_label.next_to(proc2_box, UP, buff=0.2)

        self.play(
            Create(proc1_box), Create(proc2_box), Write(proc1_label), Write(proc2_label)
        )
        self.wait(0.5)

        # Time counter
        time_text = Text("Time: 0", font_size=24)
        time_text.to_edge(LEFT).shift(UP * 2)
        self.play(Write(time_text))
        self.wait(0.3)

        # Execute schedule
        for step in schedule:
            # Update time
            new_time_text = Text(f"Time: {step['time']}", font_size=24)
            new_time_text.move_to(time_text.get_center())
            self.play(Transform(time_text, new_time_text))

            # Highlight available jobs
            animations = []
            for job_id in step["jobs"]:
                animations.append(jobs[job_id].animate.set_fill(YELLOW, opacity=0.8))

            self.play(*animations, run_time=0.5)
            self.wait(0.3)

            # Move jobs to processors
            job_copies = []
            for i, job_id in enumerate(step["jobs"]):
                box = proc1_box if i == 0 else proc2_box

                # Create copy for processor display
                job_copy = Text(job_id, font_size=20, color=WHITE)
                job_copy.move_to(box.get_center())
                job_copies.append(job_copy)

                self.play(FadeIn(job_copy), run_time=0.3)

            self.wait(0.5)

            # Mark as completed
            for i, job_id in enumerate(step["jobs"]):
                completed.add(job_id)
                self.play(
                    jobs[job_id].animate.set_fill(GREEN, opacity=0.8), run_time=0.3
                )

            # Remove from processors
            self.play(*[FadeOut(copy) for copy in job_copies], run_time=0.3)

            self.wait(0.5)

        # Final message
        final_time_text = Text(f"Time: {len(schedule)}", font_size=24)
        final_time_text.move_to(time_text.get_center())
        self.play(Transform(time_text, final_time_text))

        makespan_text = Text(
            f"Total Makespan: {len(schedule)} time units", font_size=28, color=YELLOW
        )
        makespan_text.next_to(schedule_title, DOWN, buff=0.5)
        self.play(Write(makespan_text))

        self.wait(2)


class JobGraphBuildAnimation(Scene):
    """Animated construction of a job graph"""

    def construct(self):
        title = Text("Building a Job Precedence Graph", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Step by step construction
        explanations = [
            "Jobs are unit-time tasks",
            "Arrows show precedence constraints",
            "Job must wait for all predecessors",
            "Goal: Minimize total completion time",
        ]

        positions = {
            "J1": LEFT * 2 + UP * 1.5,
            "J2": LEFT * 2 + DOWN * 1.5,
            "J3": RIGHT * 2 + ORIGIN,
        }

        jobs = {}
        labels = {}

        # Add J1
        explanation = Text(explanations[0], font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

        circle1 = Circle(radius=0.5, color=BLUE, fill_opacity=0.3)
        circle1.move_to(positions["J1"])
        label1 = Text("J1", font_size=24)
        label1.move_to(positions["J1"])

        jobs["J1"] = circle1
        labels["J1"] = label1

        self.play(Create(circle1), Write(label1))
        self.wait(0.5)

        # Add J2
        circle2 = Circle(radius=0.5, color=BLUE, fill_opacity=0.3)
        circle2.move_to(positions["J2"])
        label2 = Text("J2", font_size=24)
        label2.move_to(positions["J2"])

        jobs["J2"] = circle2
        labels["J2"] = label2

        self.play(Create(circle2), Write(label2))
        self.wait(0.5)

        # Add J3
        circle3 = Circle(radius=0.5, color=BLUE, fill_opacity=0.3)
        circle3.move_to(positions["J3"])
        label3 = Text("J3", font_size=24)
        label3.move_to(positions["J3"])

        jobs["J3"] = circle3
        labels["J3"] = label3

        self.play(Create(circle3), Write(label3))
        self.wait(0.5)

        # Add precedence constraints
        new_explanation = Text(explanations[1], font_size=24)
        new_explanation.to_edge(DOWN)
        self.play(Transform(explanation, new_explanation))
        self.wait(0.3)

        arrow1 = Arrow(
            jobs["J1"].get_center(),
            jobs["J3"].get_center(),
            buff=0.5,
            color=RED,
            stroke_width=4,
        )

        arrow2 = Arrow(
            jobs["J2"].get_center(),
            jobs["J3"].get_center(),
            buff=0.5,
            color=RED,
            stroke_width=4,
        )

        self.play(Create(arrow1))
        self.wait(0.3)
        self.play(Create(arrow2))
        self.wait(0.5)

        # Highlight constraint
        new_explanation2 = Text(explanations[2], font_size=24)
        new_explanation2.to_edge(DOWN)
        self.play(Transform(explanation, new_explanation2))

        self.play(jobs["J3"].animate.set_fill(YELLOW, opacity=0.5), run_time=0.5)

        self.play(
            Flash(jobs["J1"], color=GREEN),
            Flash(jobs["J2"], color=GREEN),
        )

        self.wait(1)

        # Final message
        new_explanation3 = Text(explanations[3], font_size=24)
        new_explanation3.to_edge(DOWN)
        self.play(Transform(explanation, new_explanation3))

        self.wait(2)


class DiamondGraphScheduling(Scene):
    """Classic diamond-shaped precedence graph"""

    def construct(self):
        title = Text("Diamond Pattern: Classic Fork-Join", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Diamond positions
        positions = {
            "A": UP * 2,
            "B": LEFT * 2,
            "C": RIGHT * 2,
            "D": DOWN * 2,
        }

        edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]

        # Create nodes
        jobs = {}
        labels = {}

        for job_id, pos in positions.items():
            circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.3)
            circle.move_to(pos)
            label = Text(job_id, font_size=28)
            label.move_to(pos)

            jobs[job_id] = circle
            labels[job_id] = label

        # Animate creation
        self.play(
            *[Create(c) for c in jobs.values()],
            *[Write(l) for l in labels.values()],
            run_time=1.5,
        )
        self.wait(0.5)

        # Create arrows
        arrows = []
        for src, dst in edges:
            arrow = Arrow(
                jobs[src].get_center(),
                jobs[dst].get_center(),
                buff=0.5,
                color=GRAY,
                stroke_width=3,
            )
            arrows.append(arrow)

        self.play(*[Create(arrow) for arrow in arrows], run_time=1)
        self.wait(1)

        # Show schedule
        schedule_text = Text("Schedule: A → (B,C) → D", font_size=28)
        schedule_text.to_edge(DOWN)
        self.play(Write(schedule_text))

        # Highlight execution order
        self.play(jobs["A"].animate.set_fill(GREEN, opacity=0.8))
        self.wait(0.5)

        self.play(
            jobs["B"].animate.set_fill(YELLOW, opacity=0.8),
            jobs["C"].animate.set_fill(YELLOW, opacity=0.8),
        )
        self.wait(0.5)

        self.play(
            jobs["B"].animate.set_fill(GREEN, opacity=0.8),
            jobs["C"].animate.set_fill(GREEN, opacity=0.8),
        )
        self.wait(0.5)

        self.play(jobs["D"].animate.set_fill(GREEN, opacity=0.8))
        self.wait(0.5)

        makespan = Text("Makespan: 3 time units", font_size=24, color=YELLOW)
        makespan.next_to(schedule_text, UP, buff=0.3)
        self.play(Write(makespan))

        self.wait(2)
