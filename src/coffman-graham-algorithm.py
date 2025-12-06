import random
import time

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
def less_than_lexicographically(a: list, b: list) -> bool:
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


def generate_random_dag(num_nodes):
    """Generates a random connected TaskGraph (DAG) with a given number of nodes."""
    tasks = list(range(1, num_nodes + 1))
    successors = {t: [] for t in tasks}

    # Establish a random topological order (which is crucial for a DAG)
    # The list 'tasks' is already ordered 1, 2, 3...

    # Randomly add edges only from node i to node j where i < j (ensuring acyclicity)
    for i in range(1, num_nodes + 1):
        # A node should have a successor to ensure connectivity is likely,
        # but let's just randomly add edges
        for j in range(i + 1, num_nodes + 1):
            if random.random() < 0.2:  # 20% chance of an edge
                successors[i].append(j)

    # Ensure connectivity (optional, but good for robust testing)
    # This basic generation ensures it's a DAG.

    G = TaskGraph(tasks=tasks, successors=successors)

    # A simple check to ensure no task is isolated (not always possible, but good try)
    if num_nodes > 1:
        all_nodes_connected = set(tasks)

        # Check if every node has a predecessor or successor
        has_connections = set()
        for u in tasks:
            if G.S(u):
                has_connections.add(u)
            for v_list in G._successors.values():
                if u in v_list:
                    has_connections.add(u)

    return G


def coffman_graham_algorithm_runtime_tests():
    print("## ⏱️ Coffman-Graham Algorithm Runtime Tests")

    # Define the input sizes (number of tasks)
    input_sizes = [10, 50, 100, 500, 1000, 2000]
    results = []

    print("| Number of Tasks (n) | Avg. Runtime (s) |")
    print("| :------------------ | :--------------- |")

    for n in input_sizes:
        # Run multiple trials for a more stable average measurement
        num_trials = 5
        total_time = 0

        for _ in range(num_trials):
            # 1. Generate a random Task Graph (DAG) of size n
            
            G = generate_random_dag(n)

            # 2. Measure the execution time
            start_time = time.perf_counter()
            try:
                coffman_graham_algorithm(G)
            except ValueError as e:
                # Catch the ValueError for "G is not a valid task graph"
                # though it shouldn't happen with the DAG generator
                print(f"Error for n={n}: {e}")
                continue
            end_time = time.perf_counter()

            total_time += end_time - start_time

        # Calculate and store the average runtime
        avg_time = total_time / num_trials
        results.append((n, avg_time))

        # Print the result immediately for real-time tracking
        print(f"| {n} | {avg_time:.6f} |")

    print("\n---")
    print("Tests complete.")


if __name__ == "__main__":
    # G = TaskGraph()

    # t1 = G.add_task()
    # t2 = G.add_task()
    # t3 = G.add_task()
    # t4 = G.add_task()
    # t5 = G.add_task()
    # t6 = G.add_task()
    # t7 = G.add_task()
    # t8 = G.add_task()

    # G.add_successor(t1, t2)
    # G.add_successor(t1, t3)

    # G.add_successor(t2, t4)
    # G.add_successor(t3, t4)

    # G.add_successor(t4, t6)
    # G.add_successor(t4, t7)
    # G.add_successor(t4, t8)

    # G.add_successor(t5, t8)

    # G.print_tasks()
    # G.print_DAG()

    # L0 = coffman_graham_algorithm(G)
    # print(f"L: {L0}")

    # print("\n\n---- test case 1\n")

    # tasks = {1, 2, 3, 4, 5, 6, 7, 8}
    # successors = {1: [2, 3], 2: [4], 3: [4], 4: [6, 7, 8], 5: [8], 6: [], 7: [], 8: []}
    # G1 = TaskGraph(tasks=tasks, successors=successors)
    # G1.print_DAG()
    # L1 = coffman_graham_algorithm(G1)
    # print(f"L: {L1}")

    # print("\n\n---- test case 2\n")

    # tasks2 = {i for i in range(1, 20)}
    # successors2 = {
    #     1: [],
    #     2: [],
    #     3: [1],
    #     4: [1],
    #     5: [2],
    #     6: [4],
    #     7: [3, 5],
    #     8: [7],
    #     9: [7],
    #     10: [8, 9],
    #     11: [8, 9],
    #     12: [8, 9],
    #     13: [10],
    #     14: [11, 12],
    #     15: [14],
    #     16: [13],
    #     17: [15, 16],
    #     18: [17],
    #     19: [6, 17],
    # }
    # G2 = TaskGraph(tasks=tasks2, successors=successors2)
    # G2.print_DAG()
    # L2 = coffman_graham_algorithm(G2)
    # print(f"L: {L2}")

    # tasks3 = [i for i in range(1, 9)]
    # successors3 = {1: [2, 3], 3: [4, 7], 5: [3], 8: [6], 6: [7]}
    # G3 = TaskGraph(tasks3, successors3)
    # G3.print_DAG()
    # L3 = coffman_graham_algorithm(G3)
    # print(f"L: {L3}")
    coffman_graham_algorithm_runtime_tests()
