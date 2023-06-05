def palindrome(s):
    if len(s) == 1:
        return 0
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return 1 + min(palindrome(s[1:]), palindrome(s[:-1]))
