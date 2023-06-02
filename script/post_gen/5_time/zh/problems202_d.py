Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(A,B,K):
    if A == 0:
        return 'b'*B
    if B == 0:
        return 'a'*A
    if K <= 0:
        return 'a'*A + 'b'*B
    if A == 1 and B == 1:
        if K == 1:
            return 'ab'
        else:
            return 'ba'
    if A == 1:
        if K == 1:
            return 'ab' + 'b'*B
        elif K == 2:
            return 'ba' + 'b'*B
        else:
            return 'b'*B + 'a'
    if B == 1:
        if K == 1:
            return 'a'*A + 'ba'
        elif K == 2:
            return 'a'*A + 'ab'
        else:
            return 'b' + 'a'*A
    if K <= 2**(A+B-1):
        return 'a' + solve(A-1,B,K-1)
    else:
        return 'b' + solve(A,B-1,K-2**(A+B-1))

=======
Suggestion 2

def dfs(a,b,k):
    if a == 0:
        return 'b'*b
    if b == 0:
        return 'a'*a
    if k <= 2**(a+b-1):
        return 'a' + dfs(a-1,b,k)
    else:
        return 'b' + dfs(a,b-1,k-2**(a+b-1))

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    # print(A, B, K)
    S = A + B
    dp = [[0 for j in range(S + 1)] for i in range(S + 1)]
    for i in range(S + 1):
        dp[i][0] = 1
        dp[i][i] = 1
    for i in range(1, S + 1):
        for j in range(1, S + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    # print(dp)
    ans = ""
    while A > 0 and B > 0:
        if K <= dp[A + B - 1][B]:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= dp[A + B - 1][B]
            B -= 1
    while A > 0:
        ans += "a"
        A -= 1
    while B > 0:
        ans += "b"
        B -= 1
    print(ans)

=======
Suggestion 4

def dfs(a,b,k):
    if a == 0:
        return 'b'*b
    if b == 0:
        return 'a'*a
    if k <= dp[a-1][b]:
        return 'a' + dfs(a-1,b,k)
    else:
        return 'b' + dfs(a,b-1,k-dp[a-1][b])

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
Suggestion 5

def main():
    A,B,K = map(int,input().split())
    S = A+B
    dp = [[0 for _ in range(B+1)] for _ in range(A+1)]
    dp[0][0] = 1
    for i in range(A+1):
        for j in range(B+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    ans = ""
    while A+B > 0:
        if A == 0:
            ans += "b"
            B -= 1
        elif B == 0:
            ans += "a"
            A -= 1
        elif K <= dp[A-1][B]:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= dp[A-1][B]
            B -= 1
    print(ans)

=======
Suggestion 6

def print_order_string(a, b, k):
    if a == 0:
        return 'b' * b
    elif b == 0:
        return 'a' * a
    elif a == 1 and b == 1:
        if k == 1:
            return 'ab'
        else:
            return 'ba'
    else:
        if k <= combination(a+b-1, a-1):
            return 'a' + print_order_string(a-1, b, k)
        else:
            return 'b' + print_order_string(a, b-1, k - combination(a+b-1, a-1))

=======
Suggestion 7

def kthString(a, b, k):
    if a == 0:
        return 'b' * b
    if b == 0:
        return 'a' * a
    # 以a开头的字符串的数量
    aNum = 1
    for i in range(a + b):
        if aNum >= k:
            break
        if aNum + (a + b - i - 1) >= k:
            break
        aNum = aNum * (a + b - i) // (i + 1)
    if aNum >= k:
        return 'a' + kthString(a - 1, b, k)
    else:
        return 'b' + kthString(a, b - 1, k - aNum)

=======
Suggestion 8

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 9

def find_k_str(a, b, k):
    if a == 0:
        return "b" * b
    elif b == 0:
        return "a" * a
    elif k <= 1:
        return "a" * a + "b" * b
    elif k > 2**(a + b):
        return ""
    elif k <= 2**(a + b - 1):
        return "a" + find_k_str(a - 1, b, k - 1)
    else:
        return "b" + find_k_str(a, b - 1, k - 2**(a + b - 1))
