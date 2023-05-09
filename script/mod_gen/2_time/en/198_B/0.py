def isPalindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return isPalindrome(string[1:-1])

if __name__ == '__main__':
    isPalindrome()