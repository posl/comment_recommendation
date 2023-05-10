Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    print(A, B, K)

=======
Suggestion 2

def main():
    A,B,K = map(int,input().split())
    S = A+B
    ans = ""
    for i in range(S):
        if A == 0:
            ans += "b"
            B -= 1
            continue
        if B == 0:
            ans += "a"
            A -= 1
            continue
        n = 1
        for j in range(A+B-1):
            n *= (A+B-j)
            n //= (j+1)
        if K <= n:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= n
            B -= 1
    print(ans)

=======
Suggestion 3

def dfs(a, b, k):
    if a == 0:
        return 'b' * b
    elif b == 0:
        return 'a' * a
    elif k <= dp[a - 1][b]:
        return 'a' + dfs(a - 1, b, k)
    else:
        return 'b' + dfs(a, b - 1, k - dp[a - 1][b])

a, b, k = map(int, input().split())

dp = [[0] * (b + 1) for _ in range(a + 1)]
dp[0][0] = 1
for i in range(a + 1):
    for j in range(b + 1):
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]

print(dfs(a, b, k))

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    if A == 0 or B == 0:
        print("a" * A + "b" * B)
        return
    # dp[a][b] = (a + b) C a
    dp = [[0] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 1
    for a in range(1, A + 1):
        dp[a][0] = 1
        for b in range(1, B + 1):
            dp[a][b] = dp[a - 1][b] + dp[a][b - 1]
    while A + B > 0:
        if A == 0:
            print("b", end="")
            B -= 1
            continue
        if B == 0:
            print("a", end="")
            A -= 1
            continue
        if K <= dp[A - 1][B]:
            print("a", end="")
            A -= 1
        else:
            print("b", end="")
            K -= dp[A - 1][B]
            B -= 1
    print()

=======
Suggestion 5

def main():
    a, b, k = map(int, input().split())
    ans = []
    for i in range(a):
        ans.append('a')
    for i in range(b):
        ans.append('b')
    ans.sort()
    ans = [''.join(ans)]
    for i in range(k-1):
        ans.append(next_permutation(ans[-1]))
    print(ans[-1])

=======
Suggestion 6

def main():
    a,b,k = map(int,input().split())
    #print(a,b,k)
    ret = ""
    for i in range(a+b):
        if a == 0:
            ret += "b"
            b -= 1
        elif b == 0:
            ret += "a"
            a -= 1
        elif k <= 2**(a+b-1):
            ret += "a"
            a -= 1
        else:
            ret += "b"
            k -= 2**(a+b-1)
            b -= 1
    print(ret)

=======
Suggestion 7

def main():
    a,b,k=map(int,input().split())
    ans=""
    for i in range(a+b):
        if a==0:
            ans+="b"
            b-=1
            continue
        if b==0:
            ans+="a"
            a-=1
            continue
        if k<=combination(a+b-1,a-1):
            ans+="a"
            a-=1
        else:
            ans+="b"
            b-=1
            k-=combination(a+b,a-1)
    print(ans)

=======
Suggestion 8

def solve():
    # 解答をここに書く
    a, b, k = map(int, input().split())
    ans = ""
    while a > 0 or b > 0:
        if a == 0:
            ans += "b"
            b -= 1
            continue
        if b == 0:
            ans += "a"
            a -= 1
            continue

        if k <= ncr(a + b - 1, b):
            ans += "a"
            a -= 1
        else:
            ans += "b"
            k -= ncr(a + b - 1, b)
            b -= 1

    print(ans)

=======
Suggestion 9

def calc_combination(a, b):
    """
    a + b 個から a 個を選ぶ組み合わせの数を返す
    """

    # a + b 個から b 個を選ぶ組み合わせの数を返す
    if a < b:
        return calc_combination(b, a)

    # 分子
    numerator = 1
    for i in range(a + 1, a + b + 1):
        numerator *= i

    # 分母
    denominator = 1
    for i in range(1, b + 1):
        denominator *= i

    return numerator // denominator

=======
Suggestion 10

def main():
    a, b, k = map(int, input().split())
    s = ''
    for i in range(a + b):
        if a == 0:
            s += 'b'
            b -= 1
            continue
        if b == 0:
            s += 'a'
            a -= 1
            continue
        if k <= num(a - 1, b):
            s += 'a'
            a -= 1
        else:
            s += 'b'
            k -= num(a - 1, b)
            b -= 1
    print(s)
