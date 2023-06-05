def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

if __name__ == '__main__':
    is_palindrome()