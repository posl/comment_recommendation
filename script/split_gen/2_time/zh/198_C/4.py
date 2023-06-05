def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
n = int(input())
print('Yes' if is_palindrome(n) else 'No')
