def isPalindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    else:
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False
