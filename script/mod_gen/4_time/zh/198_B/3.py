def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    is_palindrome()