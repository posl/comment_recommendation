def check_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
str = input()

if __name__ == '__main__':
    check_palindrome()