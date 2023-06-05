def is_palindrome(s):
    if len(s) == 1:
        return True
    else:
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True
