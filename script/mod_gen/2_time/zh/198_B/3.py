def isPalindrome(num):
    num = str(num)
    return num == num[::-1]

if __name__ == '__main__':
    isPalindrome()