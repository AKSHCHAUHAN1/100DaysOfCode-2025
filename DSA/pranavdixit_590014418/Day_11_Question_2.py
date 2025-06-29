def longest_palindrome(s):
    n = len(s)
    if n < 2:
        return s
    start = 0
    max_len = 1
    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1
    return s[start:start + max_len]

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("racecar"))
