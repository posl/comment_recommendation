def check_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[-1 - i]:
            return False
    return True
N = input()
