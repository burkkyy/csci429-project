class TaskGraph:
    def __init__(self):
        self.current_task_id = 0
        self.tasks = set()
        self.successors = {}

    def print_tasks(self):
        print(self.tasks)

    def print_DAG(self):
        print(self.successors)

    def add_task(self):
        tid = self.current_task_id

        self.tasks.add(tid)
        if tid not in self.successors:
            self.successors[tid] = []

        self.current_task_id += 1
        return tid

    def add_dependency(self, predescessor, successor):
        if predescessor not in self.successors:
            self.successors[predescessor] = []
        if successor not in self.successors:
            self.successors[successor] = []

        self.successors[predescessor].append(successor)
        self.tasks.update({predescessor, successor})

    def S(self, v):
        if v not in self.tasks:
            raise f"Task {v} is not in set of tasks"
        return self.successors[v]


def coffman_graham_algorithm(G: TaskGraph):
    pass


if __name__ == "__main__":
    G = TaskGraph()

    t1 = G.add_task()
    t2 = G.add_task()
    t3 = G.add_task()

    G.add_dependency(t1, t2)

    G.print_tasks()
    G.print_DAG()
