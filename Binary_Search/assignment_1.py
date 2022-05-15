"""
You are given list of numbers, obtained by rotating a sorted list 
an unknown number of times. Write a function to determine the 
minimum number of times the original sorted list was rotated to 
obtain the given list. Your function should have the worst-case 
complexity of O(log N), where N is the length of the list. 
You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating 
the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the 
list and adding it before the first element. E.g. rotating the 
list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged 
in the increasing order e.g. [1, 3, 5, 7].

"""

"""
1. Given a rotated sorted list that was rotated some unknown 
   number of times, we need to find the number of times it was 
   rotated. 

   ex. 'nums': A sorted rotated list e.g. [7, 9, 3, 5, 6] -> the sorted list would be [3, 5, 6, 7, 9]

   q. The function you write will return a single output called 'rotations'
       What does it represent? Give an example
       'rotations': the number of times the sorted list was rotated.
       e.g. 2. 
"""

def count_rotations(nums):