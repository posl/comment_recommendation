def isPalindrome(x):
    if len(x) == 1:
        return True
    for i in range(0, len(x)):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    isPalindrome()