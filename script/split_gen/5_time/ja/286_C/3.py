def is_palindrome(S):
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            return False
    return True
N,A,B = map(int,input().split())
S = input()
