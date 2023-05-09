def is_palindrome(s):
    return s == s[::-1]
s = input()
n = len(s)
s1 = s[:int((n-1)/2)]
s2 = s[int((n+3)/2)-1:]

if __name__ == '__main__':
    is_palindrome()