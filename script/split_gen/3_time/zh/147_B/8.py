def check_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True
