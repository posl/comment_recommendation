def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    check_palindrome()