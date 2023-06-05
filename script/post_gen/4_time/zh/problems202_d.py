Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(A, B, K):
    if A == 0:
        return 'b' * B
    if B == 0:
        return 'a' * A
    # dp[i][j]表示长度为i+j的字符串中，包含i个a和j个b的字符串的数量
    dp = [[0] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 1
    for i in range(A + 1):
        for j in range(B + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    # print(dp)
    ans = ''
    a, b = A, B
    for i in range(A + B):
        # print(a, b, dp[a - 1][b])
        if a > 0 and dp[a - 1][b] >= K:
            ans += 'a'
            a -= 1
        else:
            ans += 'b'
            K -= dp[a - 1][b]
            b -= 1
    return ans

A, B, K = map(int, input().split())
print(solve(A, B, K))

=======
Suggestion 2

def count(a,b):
    if a == 0 or b == 0:
        return 1
    else:
        return count(a-1,b) + count(a,b-1)

=======
Suggestion 3

def count(n, m):
    if n == 0 or m == 0:
        return 1
    return count(n - 1, m) + count(n, m - 1)

=======
Suggestion 4

def dfs(a,b,k):
    if a == 0:
        return 'b'*b
    if b == 0:
        return 'a'*a
    #计算以a开头的字符串的数量
    cnt = 0
    for i in range(a+1):
        cnt += comb(a+b-i-1, b)
        if cnt >= k:
            return 'a'*i + 'b' + dfs(a-i, b-1, k-cnt+comb(a+b-i-1, b))

=======
Suggestion 5

def solve(a, b, k):
    #print(a, b, k)
    #print("a", a, "b", b, "k", k)
    if a == 0:
        return "b" * b
    if b == 0:
        return "a" * a
    #print("a", a, "b", b, "k", k)
    c = comb(a - 1 + b, a - 1)
    #print("c", c)
    if k <= c:
        return "a" + solve(a - 1, b, k)
    else:
        return "b" + solve(a, b - 1, k - c)

=======
Suggestion 6

def f(a,b,k):
    if a==0:
        return "b"*b
    elif b==0:
        return "a"*a
    elif k<=1:
        return "a"*a+"b"*b
    elif k<=f(a-1,b,k-1):
        return "a"+f(a-1,b,k-1)
    else:
        return "b"+f(a,b-1,k-f(a-1,b,k-1))

=======
Suggestion 7

def main():
    A, B, K = map(int, raw_input().strip().split())
    S = A+B
    dp = [[0 for i in range(B+1)] for j in range(A+1)]
    dp[0][0] = 1
    for i in range(1, A+1):
        dp[i][0] = 1
        for j in range(1, B+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    ans = ""
    while A+B > 0:
        if A == 0:
            ans += "b"
            B -= 1
            continue
        if B == 0:
            ans += "a"
            A -= 1
            continue
        if dp[A-1][B] >= K:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= dp[A-1][B]
            B -= 1
    print ans

=======
Suggestion 8

def f(a,b,k):
    if a == 0:
        return "b"*b
    elif b == 0:
        return "a"*a
    elif k <= 1:
        return "a"*a + "b"*b
    else:
        if k <= comb(a+b-1, a-1):
            return "a" + f(a-1, b, k-1)
        else:
            return "b" + f(a, b-1, k-comb(a+b-1, a-1))

=======
Suggestion 9

def dfs(a,b,k):
    if a == 0:
        return "b"*b
    elif b == 0:
        return "a"*a
    elif k <= dp[a-1][b]:
        return "a" + dfs(a-1,b,k)
    else:
        return "b" + dfs(a,b-1,k-dp[a-1][b])

a,b,k = map(int,input().split())
dp = [[0 for _ in range(b+1)] for _ in range(a+1)]
dp[0][0] = 1
for i in range(a+1):
    for j in range(b+1):
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
print(dfs(a,b,k))

=======
Suggestion 10

def get_num(a,b,k):
    if a==0:
        return "b"*b
    if b==0:
        return "a"*a
    if k<=0:
        return "a"*a+"b"*b
    if a==1 and b==1:
        return "ab"
    if a==1 and b==2:
        return "abb"
    if a==2 and b==1:
        return "aab"
    if a==1:
        return "ab"+"a"*(b-2)+"b"
    if b==1:
        return "ba"+"b"*(a-2)+"a"
    if k==1:
        return "a"*a+"b"*b
    elif k==2:
        return "ab"+"a"*(b-1)+"b"*(a-1)
    elif k==3:
        return "ba"+"b"*(a-1)+"a"*(b-1)
    elif k==4:
        return "aab"+"a"*(b-2)+"b"
    elif k==5:
        return "aba"+"a"*(b-2)+"b"
    elif k==6:
        return "baa"+"b"*(a-2)+"a"
    else:
        return "b"+"a"*(a-1)+"b"*(b-1)

a,b,k=map(int,input().split())
print(get_num(a,b,k))
