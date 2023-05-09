def is_palindrome(s):
    return s == s[::-1]
s = input()
ans = is_palindrome(s)

if __name__ == '__main__':
    is_palindrome()