def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False
s = input()
n = len(s)
