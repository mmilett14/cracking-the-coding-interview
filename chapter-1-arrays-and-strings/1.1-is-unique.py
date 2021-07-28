# Implement an algorithm to determine if a string has all unique characters.  What if you cannot use additional data structures?

def find_unique_char(s):

    used_letters = []

    for i in range(0, len(s)):
        if s[i] in used_letters:
            return f"{s[i]} is a repeat!"
        else:
            used_letters.append(s[i])
            
    if len(used_letters) == len(s):
        return 'there are no repeated letters in this string.'
