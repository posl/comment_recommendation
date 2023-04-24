Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, sum(A[i:i + M]) + sum(range(1, M + 1)))
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, B[i + M] - B[i] + (M - 1) * A[i])
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[i] = B[i - 1] + A[i - 1]
    ans = -2 * 10 ** 5 * 2000
    for i in range(N - M + 1):
        ans = max(ans, B[i + M] - B[i])
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
        for j in range(i):
            b[i] += a[j]
    ans = 0
    for i in range(m):
        ans += (i + 1) * b[i]
    for i in range(m, n):
        ans = max(ans, ans + b[i] - b[i - m])
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        s = a[i]
        for j in range(i+1, n):
            s += a[j]
            if j - i + 1 == m:
                ans = max(ans, s)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i + M <= N:
            ans = max(ans, sum([sum(A[i:i+M][::-1][j:]) for j in range(M)]))
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[:m]))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += sum(a[i:i+m]) * (i+1)
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    B = []
    for i in range(N):
        for j in range(i, N):
            B.append(sum(A[i:j+1]))
    print(B)

=======
Suggestion 10

def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #処理
    # 累積和
    B = [0]
    for i in range(N):
        B.append(B[i] + A[i])
    #print(B)
    # 1つ目の部分列
    ans = 0
    for i in range(1, M+1):
        ans += i * A[i-1]
    #print(ans)
    # 2つ目の部分列以降
    for i in range(2, N-M+2):
        tmp = 0
        for j in range(1, M+1):
            tmp += j * A[i+j-2]
        #print(tmp)
        ans = max(ans, tmp)
    #出力
    print(ans)
