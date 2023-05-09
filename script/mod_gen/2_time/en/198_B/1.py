def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    is_palindrome()