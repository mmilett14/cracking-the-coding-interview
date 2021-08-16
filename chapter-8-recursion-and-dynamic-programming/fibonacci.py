def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i - 1)  + fibonacci(i-2)
    
def fib_memo(i):
    result = 0
    memo = [None] * (i+1)
    
    if memo[i] != None:
        return memo[i]
    
    elif (i == 1) | (i == 2):
        result = 1
        
    else:
        result = fib_memo(i-1) + fib_memo(i-2)
        
    memo[i] = result
    return result
