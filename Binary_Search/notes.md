## Problem - Rotated Lists

> You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. You can assume that all the numbers in the list are unique.
>
> Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.
>
> We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`.
>
> "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. `[1, 3, 5, 7]`.

## Example of inputs & outputs.

1. A list of size 10 rotated 3 times
2. A list of size 8 rotated 5 times.
3. A list that wasn't rotated at all.
4. A list that was rotated just once.
5. A list that was rotated `n-1` times, where `n` is the size of the list.
6. A list that was rotated `n` times (do you get back the original list here?)
7. An empty list.
8. A list containing just one element.

### Describe the linear search solution explained above problem in your own words.

1. Create a variable position with value 1
2. Compare the number at current position to the number before it
3. If the number is smaller than its predecessor, then return position.
4. Otherwise, increment position and repeat till we exhaust all the numbers.
