def check_palindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 2:
        return s[0] == s[1]
    else:
        return s[0] == s[-1] and check_palindrome(s[1:-1])

if __name__ == '__main__':
    check_palindrome()