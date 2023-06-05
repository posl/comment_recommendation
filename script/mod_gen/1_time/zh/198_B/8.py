def is_palindrome(n):
    n = str(n)
    return n == n[::-1]
print('Yes' if is_palindrome(input()) else 'No')
