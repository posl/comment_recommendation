def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

if __name__ == '__main__':
    is_palindrome()