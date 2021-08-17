# A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

# My attempt. Not correct.
def steps(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n > 3:
        return n + steps(n-1) 

# Solution from book.
def count_steps(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_steps(n-1) + count_steps(n-2) + count_steps(n-3)
      
# My attempted solution with memoization. Not correct.
def count_steps_memo(n):
    result = 0
    memo = [None] * (n + 1)
    
    if memo[n] != None:
        return memo[n]
    
    elif n < 0:
        result = 0
    
    elif n == 0:
        result = 1
        
    else:
        result = count_steps_memo(n-1) + count_steps_memo(n-2) + count_steps_memo(n-3)
    
    memo[n] = result
    return result
