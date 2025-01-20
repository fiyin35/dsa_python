## create a python function to practice recursion

## example 
# 4! = 4 *3 * 2 * 1 = 24
# 3! = 3 * 2 * 1 = 6
# 2! = 2 * 1 = 2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


factorial(10)

# iterative factorial
def iterative_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for i in range(5):
    print(i, iterative_factorial(i))

# OUTPUT
# 0 1
# 1 1
# 2 2
# 3 6
# 4 24
