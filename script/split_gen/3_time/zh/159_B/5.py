def is_strong_palindrome(s):
    n = len(s)
    if n % 2 == 0:
        return False
    if s != s[::-1]:
        return False
    if s[:(n-1)//2] != s[:(n-1)//2][::-1]:
        return False
    if s[(n+3)//2 - 1:] != s[(n+3)//2 - 1:][::-1]:
        return False
    return True
