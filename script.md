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

Let this optimal schedule be denoted as Lstar, for now its still in progress so its empty. 

The CoffmanGrahamAlgorithm states that we fill in Lstar, in reverse order. 
Bascially this means that we figure out which task to do last, and then work backwards until we finally figure out which task to do first. To illustrate this, Im will fill in L* with blanks that will eventually be replaced by some task. There are 8 tasks, so I will put 8 blanks in L*. 

By why should we do this?

Well, in a sense we are looking for tasks that "can be done later" as other tasks could be higher priority.  

For example, in this graph, its difficult to say if we should START with task 1 and 5, 1 and 8 or 8 and 5, 
But is is easy to see that task 2, 4 and 7 can be done last, as they all have no sucessors. 
In other words, task 2, 4 and 7 can be done as late as possible because no other task is waiting for them to be done
> animate defn of *sucessors*

So lets put task 2, 4 and 7 in Lstar. It should be noted that their order doesnt matter, Im simply putting them in order of their subscript for visual purposes. 

-- STOP

Now that Lstar is starting to get populated, Im going to write down the position of each task in Lstar next to each task. We will see how this is useful later.

-- break

Now, at this point, we want to figure out which task to do the fourth last,

So, how should we chose the task? Notice that for any task we choose, that task have at least one sucessor. 

What the CoffmanGrahamAlgorithm states is that we consider all tasks with successors define in L*, so in this example task T3 has its successors, T4 and T7 defined in L*, so we will consider it a potential option. This is also true for T6. Notice this is NOT true for T1, since T3 is successor is not in L*.

That was alot to unpack, but now we narrowed down which task to put in L* next.

Remeber, from this list, we want to figure out which task to do as later on as possible.

-- break

At this point, we have array of two canidate tasks. 

We reached the heart of the coffmangraham algorithm. For each task in our list of canidates, do the following. 

- Find all its successors in L* and populate some array with the indexies of its successors.
- Then we sort the indexies in decending order.

And thats it. We do this for every candiate task, and we are left with a decreasing array for each canidate task. 

In this example we only have two, but in a larger task graph we could have many candiate task arrays.

-- break

All we have to do is pick the task whose successor indecies in L* form the lexicographically smallest array.

Once we found that task, we put in L* at the last blank index.

And thats it. We repeat this process untill L* is completey filled in.





To recap the CoffmanGrahamAlgorithm,

Given a task graph,

First we make an array L* with size equal to the number of tasks.

Then we consider all tasks with no successors and put them in some order at the back on L*.

Then, until L* is filled in, do the following:

1. Consider all tasks whose successors have indices defined in L* and make it a canidate. But don't make a task a canidate if it's already in L*
2. For each candidate task, make an array with each element being its successor indices in L* sorted in decreasing order
3. Pick the candidate task with the lexicographically smallest array

At this point L* is filled in, and is the optimal schedule for the task graph

Thats the CoffmanGrahamAlgorithm algorithm.

-- STOP


Lets take a look at some psuedo code to work out its run time.

first define task graph class
