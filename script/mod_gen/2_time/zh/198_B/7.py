def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
num = int(input())
print('Yes' if is_palindrome(num) else 'No')
