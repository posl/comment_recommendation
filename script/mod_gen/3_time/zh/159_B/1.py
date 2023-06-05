def is_palindrome(s):
    return s == s[::-1]
S = input()
N = len(S)
print('Yes' if is_palindrome(S) and is_palindrome(S[:(N-1)//2]) and is_palindrome(S[(N+3)//2-1:]) else 'No')
