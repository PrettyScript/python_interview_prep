def sum1(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    final_sum = 0

    for x in range(n+1):
        final_sum += x
    return final_sum

print(sum1(10))

def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    return (n*(n+1))/2

print(sum2(10))

"""
We can compare the amount of space they take in memory or how much time it takes each function to run. 

Big O notation helps us to compare algorithms objectively

Big O describes how quickly runtime will grow relative to the input as the input gets arbitrarily large. 

Runtimes of Common Big-O Functions
1       - Constant
log(n)  - Logarithmic
n       - Linear
nlog(n) - Log Linear
n^2     - Quadratic
n^3     - Cubic
2^n     - Exponential
"""

