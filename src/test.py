DEFAULT_TASK_EXECUTION_TIME = 1
MAX_TASKS = 100


class T:
    def __init__(self, task_id, execution_time=DEFAULT_TASK_EXECUTION_TIME):
        self.task_id = task_id
        self.work_done = 0
        self.execution_time = execution_time

    def finished(self):
        return self.work_done == self.execution_time

    def work(self):
        if self.work_done >= self.execution_time:
            raise Exception("Doing work on a finished Task")
        self.work_done += 1


class G:
    def __init__(self):
        self.task_id = 0
        self.tasks = {}
        self.relations = []  # partial order

    def add_task(self, execution_time):
        if self.task_id >= MAX_TASKS:
            raise Exception("Adding too many tasks")

        new_task_id = self.task_id
        self.task_id += 1

        self.tasks[new_task_id] = T(execution_time)

        return new_task_id

    def add_dependency(self, predecessor_id, successor_id):
        self.relations.append((predecessor_id, successor_id))

    def get_number_of_tasks(self):
        return len(self.tasks)

    def S(self, task_id):
        """
        Function defined from paper:
        "The set of immediate successors of T will be denoted by S(T)" where T is some task
        """
        s = []

        for relation in self.relations:
            if relation[0] == task_id:
                s.append(relation[1])

        return s


class CoffmanGrahamAlgorithm:
    def __init__(self, task_graph: G):
        self.task_graph = task_graph
        self.L = []

    def solve_rec(self):
        pass

    def solve(self):
        r = self.task_graph.get_number_of_tasks()
        alpha = {}  # L^*
