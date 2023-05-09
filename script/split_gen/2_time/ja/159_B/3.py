def is_palindrome(s):
    return s == s[::-1]
s = input()
n = len(s)
print("Yes" if is_palindrome(s) and is_palindrome(s[:int((n-1)/2)]) and is_palindrome(s[int((n+3)/2)-1:]) else "No")
