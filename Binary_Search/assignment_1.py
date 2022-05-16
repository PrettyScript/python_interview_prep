from jovian.pythondsa import evaluate_test_cases

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

test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

def count_rotations(nums):