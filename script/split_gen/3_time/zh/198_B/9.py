def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
N = int(input())
print('Yes' if is_palindrome(N) else 'No')
