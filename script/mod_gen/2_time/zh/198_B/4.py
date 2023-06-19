def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
n = int(input())

if __name__ == '__main__':
    is_palindrome()