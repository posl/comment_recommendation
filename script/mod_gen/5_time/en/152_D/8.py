def isPalindrome(n):
    if n == 0:
        return True
    if n < 10:
        return False
    s = str(n)
    if s[0] == s[-1]:
        return True
    return False

if __name__ == '__main__':
    isPalindrome()