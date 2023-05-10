def check_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input()
