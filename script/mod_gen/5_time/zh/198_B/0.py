def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    is_palindrome()