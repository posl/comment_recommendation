def check_palindrome(s):
    if len(s) == 1:
        return True
    else:
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

if __name__ == '__main__':
    check_palindrome()