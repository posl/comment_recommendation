def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

if __name__ == '__main__':
    is_palindrome()