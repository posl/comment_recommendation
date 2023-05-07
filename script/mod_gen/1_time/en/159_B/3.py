def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    is_palindrome()