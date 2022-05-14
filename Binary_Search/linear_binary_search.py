from jovian.pythondsa import evaluate_test_cases

"""
1. State the problem clearly. Identify the input & output formats.
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algortith's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

"""


#Problem -----------------------------
"""
We need to write a program to find the position 
of a given number in a list of numbers arranged in 
decreasing order. We also need to minimize the number of 
times we access elements from the list.
"""

"""
1. IMOW: In descending order, we want to be able to access
   a given number with the least of times.     
"""

# Edge Cases -------------------------------
"""
1. The number occurs somewhere in the middle of the list cards
2. query is the first element in cards
3. query is the last element in cards
4. The list cards contains just one element, which is query
5. The list does not contain number query
6. The list cards is empty
7. The list cards contains repeating numbers.
8. The number query occurs at more than one position in cards
"""

"""
The problem statement does not specify what to do if the 
list cards does not contain the number query.
1. Read the statement again, carefully
2. Look through the examples provided with the problem
3. Ask the interviewer/platform for clarification
4. Make a reasonable assumption, state it and move forward. 

It would be a good idea to come up with 5 edge cases while
in an interview. 
"""

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

tests = []
tests.append(test)

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# card contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# card does not contain query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})


"""
Here's how we might implement it:
1. Create a variable 'position' with the value 0
2. Check whether the number at index position in card equals query
3. If it does, position is the answer and can be returned from the function
4. If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
5. If the number was not found return -1.
"""

# def locate_card(cards, query):
#     # Create a variable 'position' with the value 0
#     position = 0

#     # set up a loop for repetition
#     while True:

#         # Check if element at the current position matches the query    
#         if cards[position] == query:

#             # Answer found! Return and exit...
#             return position
        
#         # Increment the position 
#         position += 1

#         # Check if we have reached the end of the array
#         if position == len(cards):

#             # Number not found, return -1
#             return -1

# print(locate_card(**test['input']) == test['output'])
# print(tests)

"""
This function accounts for if there are no 
cards in the list
"""
# def locate_card(cards, query):
#     position = 0
#     while position < len(cards):
#         if cards[position] == query:
#             return position
#         position += 1
#     return -1

# # result = 
# result = locate_card(test['input']['cards'], test['input']['query'])
# print(result == test['output'])

"""
Time complexity: O(N)
Space complexity: O(1)
"""

"""
We will be creating a healper function that will identify multiples in 
a list
"""

"""
Great programmers write baby code, shouldn't have functions 
with more than 7 lines of code
"""

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)

    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else: 
            return "found"
    elif mid_number < query:
        return "left"
    else: 
        return "right"

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        # this will return a whole integer instead of a floating point number
        print("lo:", lo, ", hit:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1

    return -1

result = locate_card(test['input']['cards'], test['input']['query'])
print(result == test['output'])

evaluate_test_cases(locate_card, tests)