def is_palindrome(s):
    return s == s[::-1]
s = input()
n = len(s)
a = s[:(n-1)//2]
b = s[(n+3)//2-1:n]
print('Yes' if is_palindrome(s) and is_palindrome(a) and is_palindrome(b) else 'No')

if __name__ == '__main__':
    is_palindrome()