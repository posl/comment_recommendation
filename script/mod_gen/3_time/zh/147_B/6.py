def isPalindrome(s):
    if len(s) == 0:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

if __name__ == '__main__':
    isPalindrome()