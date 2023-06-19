def is_palindrome(s):
    return s == s[::-1]
s = input()
n = len(s)
a = (n-1)//2
b = (n+3)//2
print('Yes' if is_palindrome(s) and is_palindrome(s[:a]) and is_palindrome(s[b-1:]) else 'No')
