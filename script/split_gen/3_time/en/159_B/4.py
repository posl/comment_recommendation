def is_palindrome(s):
    return s == s[::-1]
s = input()
print("Yes" if is_palindrome(s) and is_palindrome(s[:(len(s)-1)//2]) and is_palindrome(s[(len(s)+1)//2:]) else "No")
