def isPalindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    isPalindrome()