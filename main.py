#Given a string, find the length of the longest substring without repeating chars

# Assumptions
# abccaab -> 3
#
# ccccccc -> 1
#
# "" = 0
#
# abcbda - > 4

# Optimal solution that uses the sliding window approach
def check_string(str):
    # Initialize variables
    length = len(str)
    dict ={}
    left = right = total = 0
    # If the string has only one or less characters just return the current length
    if length <= 1:
        return length
    else:
        # While the right pointer is less than the length of the string (-1 not needed)
        while right < length:
            # If the dictionary does not contain the letter at index p or
            # if the letter's index is less than the left pointer (outside the current substring)
            if str[right] not in dict or dict.get(str[right]) < left:
                dict[str[right]] = right
                right += 1
            else:
                # Otherwise move the left pointer forward based on the index of the last repeated
                # character found in the dictionary
                left = dict.get(str[right]) + 1
            # The max length of the current string is the difference between right and left pointers
            curr_max = right - left
            # Total is the Max between curr_max and the running total
            total = max(curr_max, total)
        return total

input = 'abcbda'
print(check_string(input))




#Original solution bruteforce that may touch elements more than once since it slides back when trying to find the longest sentence

# def check_string(str):
#     #Initialize variables
#     length = len(str)
#     p = total = curr_max = 0
#     dict = {}
#     # While pointer p is within the length of the string
#     while p < length:
#        # If the character at index p is not in the dictionary, add it and move p to the right
#         if str[p] not in dict:
#             dict[str[p]] = p
#             p += 1
#             # curr_max is equal to the current length of the dictionary
#             curr_max = len(dict)
#         # Otherwise
#         else:
#             # Move pointer one character to the right from the dupe
#             p = dict.get(str[p]) + 1
#             # Clear the dictionary
#             dict.clear()
#             # Add the character to the dictionary to begin the new substring
#             dict[str[p]]= p
#             p += 1
#         total = max(total, curr_max)
#     return total
# 
# 
# input = 'abcbda'
# print(check_string(input))