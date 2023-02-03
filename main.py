#Given a string, find the length of the longest substring without repeating chars

# Assumptions
# abccaab -> 3
#
# ccccccc -> 1
#
# "" = 0
#
# abcbda - > 4

def check_string(str):
    length = len(str)
    dict ={}
    left = right = longest_substring = 0

    if length <= 1:
        return length
    else:
        while right < length:
            if str[right] not in dict:
                dict[str[right]] = right
                right += 1
            else:
                if dict.get(str[right]) < left:
                    dict[str[right]] = right
                    right += 1
                else:
                    left = dict.get(str[right]) + 1

            curr_max = right - left
            longest_substring = max(curr_max, longest_substring)
        return longest_substring

input = 'abcbda'
print(check_string(input))





#Original solution bruteforce that may touch elements more than once since it slides back when trying to find the longest sentence

# def check_string(str):
#     length = len(str)
#     p = total = curr_max = 0
#     dict = {}
#
#     while p < length:
#         if str[p] not in dict:
#             dict[str[p]] = p
#             p += 1
#             curr_max = len(dict)
#         else:
#             p = dict.get(str[p]) + 1 #Move one character to the right from the dupe
#             dict.clear()
#             dict[0]=str[p]
#             p += 1
#         total = max(total, curr_max)
#     return total
#
#
# input = 'abcbda'
# print(check_string(input))