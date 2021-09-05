# Staircase

## Recursion

### **Problem Statement - (Recursion) - Repeat Exercise**

A child is running up a staircase and can hop either 1 step, 2 steps or 3 steps at a time. Given that the staircase has a total `n` steps, write a function to count the number of possible ways in which child can run up the stairs.

For e.g.

- `n == 1` then `answer = 1`
- `n == 3` then `answer = 4`The output is `4` because there are four ways we can climb the staircase:
    - 1 step + 1 step + 1 step
    - 1 step + 2 steps
    - 2 steps + 1 step
    - 3 steps
- `n == 5` then `answer = 13`

**Hint:** You would need to make use of the [Inductive Hypothesis](https://en.wikipedia.org/wiki/Mathematical_induction#Description), which comprises of the following two steps:

1. **The Inductive Hypothesis**: Calculate/assume the results for base case. In our problem scenario, the base cases would be when n = 1, 2, and 3.
2. **The Inductive Step**: Prove that for every 𝑛 >= 3, if the results are true for  n, then it holds for (𝑛+1) as well. In other words, assume that the statement holds for some arbitrary natural number n, and prove that the statement holds for (n+1).

## Caching

You can notice that even for a small number of staircases (here 5), we are calling `n=3` and `n=2` multiple times. Each time we call a method, additional time is required to calculate the solution. In contrast, instead of calling on a particular value of `n` again and again, we can **calculate it once and store the result** to speed up our program.

> Which data structure are you thinking to store the results?

Your job is to use any data-structure that you have used until now to write a faster implementation of the function you wrote earlier while using recursion.