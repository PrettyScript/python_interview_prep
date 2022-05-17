from jovian.pythondsa import evaluate_test_case

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

def count_rotations_linear(nums):
    # what is the initial value of position?
    position = 0

    # when should the loop be terminated? 
    while position < len(nums):

        # Success critera: check whether the number at the current position 
        if position > 0 and nums[position] < nums[position-1]:
            return position

        # Move to the next position
        position += 1

    # What if none of the positions passed
    return 0

    
evaluate_test_case(count_rotations_linear, test)



