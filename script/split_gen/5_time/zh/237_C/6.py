def is_palindrome(s):
    return s == s[::-1]
s = input()
l = len(s)
s1 = s[0:(l-1)//2]
s2 = s[(l+3)//2-1:l]
