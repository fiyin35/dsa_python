## The fibonacci numbers are the numbers of the following sequence of integer values
## 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

def fibonacci(n):
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(9))

# An iterative solution
def fib(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new