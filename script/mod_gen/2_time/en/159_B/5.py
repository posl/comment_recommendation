def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False
S = input()
N = len(S)

if __name__ == '__main__':
    is_palindrome()