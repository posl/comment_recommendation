def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False
s = input()
n = len(s)

if __name__ == '__main__':
    is_palindrome()