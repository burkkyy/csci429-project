# csci 492 presentation script

## Structure

1. Introduction
  a. Introduce an easier form of the problem and give naive solutions, showing that its not super clear how to find the optimal solution
  b. Introduce the paper, and introduce / define the problem that the paper solved
2. Show the trial 1-Processor case
3. 2-Processor CoffmanGrahamAlgorithm
  a. The problem setup
  b. Naive attempt (Greedy algorithm) and give a counter example
  c. Explain the algorithm and give examples
  d. Show proof of its correctness
  e. Show proof of its optimality
4. 3-Processor case (?)
4. Conclusion

# Script

## Introduction / 1 processor case

-- begin

Imagine you have a list of chores and errands you had to complete by the end of the day. You need to buy groceries for dinner, cook dinner, clean up afterward, do your laundry, and put the laundry away. 
> animate the list of jobs as a checklist

Notice that some of these tasks depend on others, ie you cant cook dinner until you buy the groceries and you cant put your laundry away before its washed and dried.
You want to get everything done as quickly as possible — the sooner you finish, the sooner you can relax and watch youtube videos.
> animate animate the list of jobs in the checklist forming a graph DAG

In what order would you do these tasks?
Well, looking at the graph its trival to see that we came pick a task with no dependencies to work on. Once done, we just repeat, picking tasks with no depencies until all tasks are done, and we are done.
> animate picking tasks with no dependencies and doing the next one

As for the time complexity of this approach, skipping over some details, if we are give a set of tasks, at each step in time we are simply searching for one task with no depencies. In a worst case, we could be seaching over all the tasks. So this naive approach is O(n), where n is the number of tasks   

-- pause

But lets imagine now that we have a lot of tasks, too many for just us to handle. So we call another person, maybe a friend or sibling. Now that there are two people working on tasks, how should you divide up the tasks between you and your partner?

Before we look at the solution, lets make this problem easier to generalize. We can refer to tasks as T1, T2 and so on. 

We'll call the two people P1 and P2. In computer science terms, more generally, we can think of them as processors, that can process tasks. We'll also keep track of the tasks P1 and P2 are working on, currently it can be seen as empty.

We'll also use the greek letter mu to represet the current time step. For now, we’ll assume that each task takes exactly one time step to complete. Later on we’ll explore what happens when tasks take different amounts of time.

> break
Lastly, the schedule produced by P1 and P2 we shall call L, it simply keeps track of the order in which tasks are done in.

Now, let’s try processing these tasks using the same method as before — at each time step, we pick any task that has no remaining dependencies. Once a task is completed, we update the graph and continue choosing the next available tasks until everything is done.

All the tasks are done, and we can see that it took 5 units of time to complete all 8 tasks. But can we do better? If we go back, we can see that there were two time steps where P2 wasn't doing any work, so maybe there’s a more efficient way to schedule everything.

This question was studied in the early 1970s, and an algorithm was found by Edward Coffman and Ronald Graham in their 1971 paper `Optimal Scheduling for Two-Processor Systems`. In this presentation I will be refering to their method as the CoffmanGrahamAlgorithm.

-- end

## 2-Processor CoffmanGrahamAlgorithm

-- begin

So, what is the Coffman–Graham Algorithm?
Well, in their paper is written in a way that's hard to understand, but here’s the full definition, exactly as it appears in the original paper.
>animate algorithm

We won’t be using this formal definition, for now. Instead, we’ll step through an example to build an intuitive understanding of how the algorithm works. 

Lets go back to the same graph we had before. 
> animate same graph as DAGScene

Why was our schdule not optimal?
