def isPalindrome(number):
    string = str(number)
    if string == string[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    isPalindrome()