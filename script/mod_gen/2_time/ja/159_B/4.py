def is_palindrome(s):
    return s == s[::-1]
S = input()
N = len(S)
S1 = S[:(N-1)//2]
S2 = S[(N+3)//2-1:]
print('Yes' if is_palindrome(S) and is_palindrome(S1) and is_palindrome(S2) else 'No')
