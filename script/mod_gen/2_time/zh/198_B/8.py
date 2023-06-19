def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

if __name__ == '__main__':
    is_palindrome()