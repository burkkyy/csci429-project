class TaskGraph:
    def __init__(self, tasks=None, successors=None):
        self._current_task_id = 1
        self._tasks = set()
        self._successors = {}

        if tasks is not None and successors is not None:
            self._tasks = set(tasks)
            for task in tasks:
                self._successors[task] = []
            for task, succ_list in successors.items():
                self._successors[task] = list(succ_list)
            self._current_task_id = max(self._tasks) + 1 if self._tasks else 1
        elif tasks is not None:
            for t in tasks:
                self._tasks.add(t)
                if t not in self._successors:
                    self._successors[t] = []
            self._current_task_id = max(self._tasks) + 1 if self._tasks else 1

    def print_tasks(self):
        print(f"tasks: {self._tasks}")

    def print_DAG(self):
        print(f"G: {self._successors}")

    def number_of_tasks(self):
        return len(self._tasks)

    def tasks(self):
        return self._tasks

    def add_task(self):
        tid = self._current_task_id

        self._tasks.add(tid)
        if tid not in self._successors:
            self._successors[tid] = []

        self._current_task_id += 1
        return tid

    def add_successor(self, predecessor, successor):
        if predecessor not in self._successors:
            self._successors[predecessor] = []
        if successor not in self._successors:
            self._successors[successor] = []

        self._successors[predecessor].append(successor)
        self._tasks.update({predecessor, successor})

    def S(self, v) -> list:
        if v not in self._tasks:
            raise ValueError(f"Task {v} is not in the set of tasks")
        return self._successors[v]


# helper function for coffman_graham_algorithm, O(n) where n = max(len(a),len(b))
def less_than_lexicographically(a, b) -> bool:
    if len(a) == 0 and len(b) == 0:
        return False
    if len(a) == 0:
        return True

    min_len = min(len(a), len(b))

    for i in range(min_len):
        if a[i] < b[i]:
            return True
        elif a[i] > b[i]:
            return False

    return len(a) < len(b)


def coffman_graham_algorithm(G: TaskGraph):
    r = G.number_of_tasks()
    k = 1
    alpha = {}

    # (a) choose first task with S(T) = {}
    for T in G.tasks():  # O(n)
        if not G.S(T):
            alpha[T] = k
            k += 1

    if not alpha:
        raise ValueError("G is not a valid task graph")

    # (b)
    while k <= r:  # In worst case, O(n). Overall O(n^3).
        N = {}
        for T in G.tasks():  # O(n)
            if T in alpha:
                continue

            all_successors_defined = True
            S_T = G.S(T)

            for t in S_T:  # In worst case, O(n)
                if t not in alpha:
                    all_successors_defined = False
                    break

            if all_successors_defined:
                N[T] = sorted([alpha[t] for t in S_T], reverse=True)

        if not N:
            raise ValueError("G is not a valid task graph")

        # print(f"\tN: {N}")

        current_min_n = None
        for n in N:
            if current_min_n == None:
                current_min_n = n
                continue

            lt_eq_lex = less_than_lexicographically(N[n], N[current_min_n])
            # print(
            #     f"\t N[{n}] < N[{current_min_n}] = {lt_eq_lex} -> {N[n]} < {N[current_min_n]} = {lt_eq_lex}"
            # )
            if lt_eq_lex:
                current_min_n = n
            elif N[n] == N[current_min_n]:
                if n < current_min_n:
                    current_min_n = n

            # print(f"n: {n}")

        alpha[current_min_n] = k
        k += 1

        # print("--------")
        # print(f"k: {k}")
        # print(f"\tcurrent_min_n: {current_min_n}")
        # print(f"\tN: {N}")
        # print(f"\tcurrent alpha: {alpha}")
        # print("--------\n")

    schedule = sorted(alpha.keys(), key=lambda task: alpha[task])
    return schedule[::-1]


if __name__ == "__main__":
    G = TaskGraph()

    t1 = G.add_task()
    t2 = G.add_task()
    t3 = G.add_task()
    t4 = G.add_task()
    t5 = G.add_task()
    t6 = G.add_task()
    t7 = G.add_task()
    t8 = G.add_task()

    G.add_successor(t1, t2)
    G.add_successor(t1, t3)

    G.add_successor(t2, t4)
    G.add_successor(t3, t4)

    G.add_successor(t4, t6)
    G.add_successor(t4, t7)
    G.add_successor(t4, t8)

    G.add_successor(t5, t8)

    G.print_tasks()
    G.print_DAG()

    L0 = coffman_graham_algorithm(G)
    print(f"L: {L0}")

    print("\n\n---- test case 1\n")

    tasks = {1, 2, 3, 4, 5, 6, 7, 8}
    successors = {1: [2, 3], 2: [4], 3: [4], 4: [6, 7, 8], 5: [8], 6: [], 7: [], 8: []}
    G1 = TaskGraph(tasks=tasks, successors=successors)
    G1.print_DAG()
    L1 = coffman_graham_algorithm(G1)
    print(f"L: {L1}")

    print("\n\n---- test case 2\n")

    tasks2 = {i for i in range(1, 20)}
    successors2 = {
        1: [],
        2: [],
        3: [1],
        4: [1],
        5: [2],
        6: [4],
        7: [3, 5],
        8: [7],
        9: [7],
        10: [8, 9],
        11: [8, 9],
        12: [8, 9],
        13: [10],
        14: [11, 12],
        15: [14],
        16: [13],
        17: [15, 16],
        18: [17],
        19: [6, 17],
    }
    G2 = TaskGraph(tasks=tasks2, successors=successors2)
    G2.print_DAG()
    L2 = coffman_graham_algorithm(G2)
    print(f"L: {L2}")
