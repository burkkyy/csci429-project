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

-- pause

But lets imagine now that we have a lot of tasks, too many for just us to handle. So we call another person, maybe a friend or sibling. Now that there are two people working on tasks, how should you divide up the tasks between you and your partner?

If we try the method before, we dont always necessarily pick the most optimal schedule. 
**Show that naive method does not work with 2 processors**
> animate the naive 1 processor case

> Go through why method before does not work

So what is the most optimal scheduling strategy?
This question was studied in the early 1970s, and an algorithm was found by Edward Coffman and Ronald Graham in their 1971 paper `Optimal Scheduling for Two-Processor Systems`. In this presentation I will be refering to this algorithm as the CoffmanGrahamAlgorithm.


-- end

## 2-Processor CoffmanGrahamAlgorithm

Before I show you the CoffmanGrahamAlgorithm
