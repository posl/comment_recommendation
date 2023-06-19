Synthesizing 10/10 solutions

=======
Suggestion 1

def calc(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    if n > r:
        return calc(n-1, r) + calc(n-1, r-1)

=======
Suggestion 2

def f(a,b,k):
    if a == 0:
        return 'b'*b
    elif b == 0:
        return 'a'*a
    elif k <= 1:
        return 'a'*a+'b'*b
    else:
        if k <= (a+b):
            return 'a'+f(a-1,b,k-1)
        else:
            return 'b'+f(a,b-1,k-a-b)

a,b,k = map(int, input().split())
print(f(a,b,k))

=======
Suggestion 3

def dfs(a, b, k):
    if a == 0:
        return 'b' * b
    if b == 0:
        return 'a' * a
    num = comb[a + b - 1][b]
    if k <= num:
        return 'a' + dfs(a - 1, b, k)
    else:
        return 'b' + dfs(a, b - 1, k - num)

=======
Suggestion 4

def solve(A,B,K):
    def dfs(a,b,k):
        if a==0:
            return 'b'*b
        elif b==0:
            return 'a'*a
        elif k<=dp[a-1][b]:
            return 'a'+dfs(a-1,b,k)
        else:
            return 'b'+dfs(a,b-1,k-dp[a-1][b])
    dp=[[1]*(B+1) for _ in range(A+1)]
    for i in range(1,A+1):
        for j in range(1,B+1):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dfs(A,B,K)
A,B,K=map(int,input().split())
print(solve(A,B,K))

=======
Suggestion 5

def getPermutation(n,k):
    if n==1:
        return '1'
    nums = [i for i in range(1,n+1)]
    res = ''
    while n>0:
        if k==1:
            res += ''.join(str(i) for i in nums)
            break
        else:
            if k==factorial(n):
                nums.reverse()
                res += ''.join(str(i) for i in nums)
                break
            else:
                if k%factorial(n-1)==0:
                    index = k/factorial(n-1)
                else:
                    index = k/factorial(n-1)+1
                res += str(nums[index-1])
                nums.remove(nums[index-1])
                k = k%factorial(n-1)
                n -= 1
    return res

=======
Suggestion 6

def solve():
    A, B, K = map(int, input().split())
    import math
    def comb(a, b):
        return math.factorial(a + b) // (math.factorial(a) * math.factorial(b))
    ans = ''
    while A + B > 0:
        if A == 0:
            ans += 'b'
            B -= 1
            continue
        if B == 0:
            ans += 'a'
            A -= 1
            continue
        if K <= comb(A - 1, B):
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            K -= comb(A - 1, B)
            B -= 1
    print(ans)

=======
Suggestion 7

def solve():
    A, B, K = map(int, input().split())
    S = A + B
    dp = [[0 for _ in range(B + 1)] for _ in range(A + 1)]
    dp[0][0] = 1
    for i in range(A + 1):
        for j in range(B + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    ans = ""
    while A > 0 and B > 0:
        if K <= dp[A - 1][B]:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= dp[A - 1][B]
            B -= 1
    while A > 0:
        ans += "a"
        A -= 1
    while B > 0:
        ans += "b"
        B -= 1
    print(ans)

solve()

=======
Suggestion 8

def main():
    A,B,K = map(int, input().split())
    if A == 0:
        print("b"*B)
        return
    if B == 0:
        print("a"*A)
        return
    dp = [[0]*(B+1) for _ in range(A+1)]
    dp[0][0] = 1
    for i in range(A+1):
        for j in range(B+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    ans = ""
    while A > 0 and B > 0:
        if K <= dp[A-1][B]:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= dp[A-1][B]
            B -= 1
    ans += "a" * A
    ans += "b" * B
    print(ans)

=======
Suggestion 9

def solve(a, b, k):
    if k == 0:
        return 'a' * a + 'b' * b
    elif a == 0:
        return 'b' + 'a' * a + 'b' * b
    elif b == 0:
        return 'a' + 'a' * a + 'b' * b
    elif k <= combi(a + b - 1, a - 1):
        return 'a' + solve(a - 1, b, k)
    else:
        return 'b' + solve(a, b - 1, k - combi(a + b - 1, a - 1))

=======
Suggestion 10

def main():
    a,b,k = map(int,input().split())
    s = a+b
    dp = [[0]*(b+1) for i in range(a+1)]
    dp[0][0] = 1
    for i in range(a+1):
        for j in range(b+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    ans = ""
    while a > 0 and b > 0:
        if dp[a-1][b] >= k:
            ans += "a"
            a -= 1
        else:
            ans += "b"
            k -= dp[a-1][b]
            b -= 1
    while a > 0:
        ans += "a"
        a -= 1
    while b > 0:
        ans += "b"
        b -= 1
    print(ans)
