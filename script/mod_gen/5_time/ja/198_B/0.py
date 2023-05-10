def check_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[-1 - i]:
            return False
    return True
N = input()

if __name__ == '__main__':
    check_palindrome()