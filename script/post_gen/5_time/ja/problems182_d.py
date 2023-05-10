Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [2, -1, -2]
    #N = len(A)
    #print(N, A)
    #print('----------')
    #print(N, A)
    #print(

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    pos = 0
    for a in A:
        pos += a
        ans = max(ans, pos)
    print(ans)
main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += A[i]
        ans = max(ans, tmp)
    print(ans)
main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    x = 0
    for i in range(N):
        x += A[i]
        ans = max(ans, x)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    max = 0
    for i in range(N):
        sum += A[i]
        if max < sum:
            max = sum
    print(max)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    #print(s)
    max_p = 0
    max_s = 0
    for i in range(n+1):
        if s[i] > max_s:
            max_s = s[i]
        if max_p < max_s:
            max_p = max_s
    print(max_p)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cur = 0
    for i in range(n):
        cur += a[i]
        ans = max(ans, cur)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    maxs = [0] * (n + 1)
    for i in range(n):
        maxs[i + 1] = max(maxs[i], s[i + 1])
    ans = 0
    x = 0
    for i in range(n):
        ans = max(ans, x + maxs[i + 1])
        x += s[i + 1]
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(0)

    # dp[i] = 動作開始時から終了時までのロボットの座標の最大値
    dp = [0] * (N+1)
    dp[0] = 0
    for i in range(N):
        dp[i+1] = dp[i] + A[i]
    #print(dp)

    # dp2[i] = 動作開始時から終了時までのロボットの座標の最大値
    dp2 = [0] * (N+1)
    dp2[0] = 0
    for i in range(N):
        dp2[i+1] = dp2[i] + dp[i+1]
    #print(dp2)

    # dp3[i] = 動作開始時から終了時までのロボットの座標の最大値
    dp3 = [0] * (N+1)
    dp3[0] = 0
    for i in range(N):
        dp3[i+1] = dp3[i] + dp2[i+1]
    #print(dp3)

    print(max(dp3))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    max_x = 0
    for i in range(n):
        x += a[i]
        max_x = max(max_x, x)
    print(max_x)
