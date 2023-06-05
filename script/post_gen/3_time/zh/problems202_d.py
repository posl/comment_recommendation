Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def calc_combination(a, b):
    if a == 0 or b == 0:
        return 1
    return calc_combination(a - 1, b) + calc_combination(a, b - 1)

=======
Suggestion 3

def dfs(a,b,k):
    if a==0:
        return 'b'*b
    if b==0:
        return 'a'*a
    i=comb[a+b-1][b]
    if k<=i:
        return 'a'+dfs(a-1,b,k)
    else:
        return 'b'+dfs(a,b-1,k-i)

A,B,K=map(int,input().split())
comb=[[0 for i in range(B+1)] for j in range(A+B+1)]
for i in range(A+B+1):
    comb[i][0]=1
    for j in range(1,min(i,B+1)):
        comb[i][j]=comb[i-1][j-1]+comb[i-1][j]
print(dfs(A,B,K))

=======
Suggestion 4

def comb(n, m):
    if n == m or m == 0:
        return 1
    elif 0 < m < n:
        return comb(n-1, m-1) + comb(n-1, m)
    else:
        return 0

=======
Suggestion 5

def solve(A, B, K):
    if A == 0:
        return 'b' * B
    elif B == 0:
        return 'a' * A
    elif K == 1:
        return 'a' * A + 'b' * B
    elif K == 2 ** (A + B):
        return 'b' * B + 'a' * A
    elif K <= 2 ** (A + B - 1):
        return 'a' + solve(A - 1, B, K - 1)
    else:
        return 'b' + solve(A, B - 1, K - 2 ** (A + B - 1))

=======
Suggestion 6

def solve(A, B, K):
    if A == 0:
        return 'b'*B
    elif B == 0:
        return 'a'*A
    else:
        if K <= comb(A+B-1, B-1):
            return 'a' + solve(A-1, B, K)
        else:
            return 'b' + solve(A, B-1, K-comb(A+B-1, B-1))

=======
Suggestion 7

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 8

def permutation(a,b,k):
    if a == 0 or b == 0:
        return "a"*a + "b"*b
    elif k <= 0:
        return "a"*a + "b"*b
    else:
        count = 1
        for i in range(1,a+b+1):
            count *= i
        for i in range(1,a+1):
            count /= i
        for i in range(1,b+1):
            count /= i
        if k <= count:
            return "a" + permutation(a-1,b,k)
        else:
            return "b" + permutation(a,b-1,k-count)

=======
Suggestion 9

def getStr(A, B, K):
    if A == 0:
        return "b"*B
    if B == 0:
        return "a"*A
    if K <= 1:
        return "a"*A + "b"*B
    if K > 1:
        return getStr(A-1, B, K-1) + getStr(A, B-1, K-1)

A, B, K = map(int, input().split())
print(getStr(A, B, K))
