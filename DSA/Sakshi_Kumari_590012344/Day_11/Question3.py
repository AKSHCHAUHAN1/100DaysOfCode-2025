Your task: Count the total number of palindromic substrings in a string.

def count_palindromic_substrings(s):
    count = 0
    def expand(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)
        expand(i, i + 1)
    return count
