"""
O(1) Constant
"""

"""
Doesn't matter how many values are in the list, this function will always print out one value
"""
def func_constant(values):
    print(values[0])

lst = [1,2,4]
func_constant(lst)

"""
O(n) Linear
"""

"""
A list of n items will print n times
"""
def func_lin(lst):
    for val in lst:
        print(val)

func_lin(lst)

"""
O(n^2) Quadratic
"""

"""
For n items in a list, we will have to perform an action n times so n * n or n^2
"""
def func_quad(lst):
    for item_1 in lst:
        for item_2 in lst:
            print(item_1, item_2)

func_quad(lst)

"""
O(n)
"""
def print_once(lst):
    for val in lst:
        print(val)

print_once(lst)

"""
O(2n) or O(n), we are dropping the constant since 2 x infinity is the same as n
"""
def print_2(lst):
    for val in lst:
        print(val)

    for val in lst:
        print(val)

print_2(lst)

def comp(lst):
    print(lst[0]) #O(1)

    midpoint = int(len(lst)/2) #O(n/2) same as O( 1/2 * n)



    for val in lst[:midpoint]:
        print(val)

    for x in range(10): #O(10)
        print("hello world")

lst = [1,2,3,4,5,6,7,8,9,10]
comp(lst)

"""
We would have to add up all the constants
O(1 + n/2 + 10)
Simplifies as O(n)
"""

def matcher(lst, match):

    for item in lst:
        if item == match:
            return True

    return False

print(matcher(lst, 1)) #O(1) best case
print(matcher(lst, 11)) #O(n) worse case because you have to check each value

"""
Space Complexity: O(n), we have to take in n amount of space in memory
"""
def create_list(n):

    new_list = []

    for num in range(n):
        new_list.append('new')
    
    return new_list

print(create_list(5))

"""
Space complexity O(1) since we are only saving one item in memory
"""
def printer(n):

    for x in range(10):
        print("Hello World!")

printer(10)