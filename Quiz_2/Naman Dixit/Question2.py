def first_non_repeating(s):
    char_count = {}

    # Step 1: Count frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Step 2: Find the first character with count 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1  # No non-repeating character found

# Example usage
s = input("Enter a string: ")
index = first_non_repeating(s)

if index == -1:
    print("No non-repeating character found.")
else:
    print(f"Index of first non-repeating character: {index} ('{s[index]}')")
