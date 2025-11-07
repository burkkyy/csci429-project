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

Imagine you have a list of tasks to complete by the end of the day. Lets say you need to buy some groceries, make dinner, clean up after dinner and do your laundry. You want to complete all these tasks in the least amount of time, the sooner you finish, the sooner you can relax and watch youtube videos.
> animate the list of jobs as a checklist

Notice that some of these tasks depend on others. 
For example, you cant clean the kichen until you cook dinner, and you cant cook dinner until you buy the groceries and so on. Formally speaking, given some task, the tasks that come before it are called its predessessors, and the tasks that immediatly come before it are called its immediate predessessors. 

In this example the predessesors of cleaning the kicken, is cooking dinner and buying groceries, and the immediate predesseor is cooking dinner.
> animate animate the list of jobs in the checklist forming a graph DAG

In what order would you do these tasks?
Well, looking at the graph one naive approach would be to pick a task with no predessessors to work on. Once done, remove the task and we repeat, working on tasks and then removing them until we are all done.
> animate picking tasks with no dependencies and doing the next one

For this naive approach, lets take a look at what the sudo code may look like.  if we are give a set of tasks, at each step in time we are searching for a task with no predessessors. As for the time complexity of this approach, skipping over some details this would be big O of n squared, where n is the number of tasks   

-- pause

But now, lets imagine that we have a lot of tasks, too many for just one person to handle. So we call up someone else, maybe a friend or sibling.
Now that there are two people working on tasks, how should you divide up the tasks between you and your partner?

Before we look at the solution, lets formalize this problem so its easier to generalize.
We can refer to tasks as T subscipt 1, T subscipt 2 and so on. 

We'll call the two people working on tasks P1 and P2. In computer science terms, we can think of them as processors. We'll also keep track of the tasks P1 and P2 are working on, currently it can be seen as empty.

We'll also use the greek letter mu to represet the current time step. For now, we’ll assume that each task takes exactly one time step to complete. Later on we’ll explore what happens when each task takes a different amount of time.

> break

Lastly, the schedule produced by P1 and P2 we shall call L. It will keep track of the order in which tasks are done in.

-- STOP

Now, let’s try processing these tasks using the same method as before — at each time step, we pick any task that has no remaining immediate predessessors. Once a task is completed, we update the graph and continue choosing the next available tasks until everything is done.

All the tasks are done, and we can see that it took 5 units of time to complete all 8 tasks. But can we do better? If we go back, we can see that there were two time steps where P2 wasn't doing any work, so maybe there’s a more efficient way to schedule tasks.

This question was studied in the early 1970s, and an algorithm was found by Edward Coffman and Ronald Graham in their 1971 paper `Optimal Scheduling for Two-Processor Systems`. 
I will be refering to their method as the CoffmanGrahamAlgorithm.

## 2-Processor CoffmanGrahamAlgorithm

Here is the full definition of the CoffmanGrahamAlgorithm, as it appears in the original paper.
>animate algorithm

The full definition is a lot to take in, so we won’t be using this formal definition for now.

Instead, we’ll step through an example to build an intuitive understanding of how the algorithm works. 

-- STOP

Lets go back to the same graph we had before. 
> animate same graph as DAGScene

Why was our schdule not optimal? Just to prove to you that the previous schedule was not optimal, I will quickly show a better schedule, in fact the most optimal one.
> animate most optimal schedule

-- break

Notice that at each time step, both processors are working on a task. This means we reached the most optimal schedule, since there was never a time where we couldve done an additional task. 

But anyways, how do we find the optimal schedule in the general case? Well, notice that at each time step, we get to pick tasks to work on.
A nature follow up question would be, during each time step, how do we figure out which tasks to pick for the optimal schedule?

-- STOP

Let this optimal schedule be denoted as Lstar, for now its still in progress so its empty. The CoffmanGrahamAlgorithm states that we fill in Lstar, in reverse order. 
Bascially this means that we figure out which task to do last, and then work backwards until we finally figure out which task to do first. 
By why should we do this?

Well, in a sense we are looking for tasks that "can be done later" as other tasks could be higher priority.  

For example, in this graph, its difficult to say if we should START with task 1 and 5, 1 and 8 or 8 and 5, 
But is is easy to see that task 2, 4 and 7 can be done last, as they all have no sucessors. 
In other words, task 2, 4 and 7 can be done as late as possible because no other task is waiting for them to be done
> animate defn of *sucessors*

So lets put task 2, 4 and 7 in Lstar. It should be noted that their order doesnt matter, Im simply putting them in order of their subscript for visual purposes. 

-- STOP

Now we want to figure out which task is the least priority to put in the third last slot of Lstar... which task should it be?

-- break

CoffmanGrahamAlgorithm states blah blah blah
