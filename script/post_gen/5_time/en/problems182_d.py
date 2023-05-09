Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    s.sort()
    ans = 0
    for i in range(n):
        ans += s[i + 1] - s[i]
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    x = 0
    for a in A:
        x += a
        ans = max(ans, x)
    print(ans)
solve()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    x = 0
    max_x = 0
    for i in range(N):
        x += A[i]
        max_x = max(max_x, x)
    print(max_x)

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
        ans = max(ans, s)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    s.sort()
    ans = 0
    for i in range(n):
        ans = max(ans, s[i+1] - s[i])
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    pos = 0
    for i in range(N):
        pos += A[i]
        ans = max(ans, pos)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
        ans = max(ans, s)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    s.sort()
    ans = 0
    for i in range(n):
        ans = max(ans, s[i+1] - s[i])
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1. 累積和を求める
    # 2. 累積和の最大値を求める
    # 3. 1 + 2 の最大値を求める
    # 4. 3 の最大値を求める
    # 5. 4 の最大値を出力する
    B = []
    tmp = 0
    for i in range(N):
        tmp += A[i]
        B.append(tmp)

    print(max(B))

=======
Suggestion 10

def robot(a):
    s = 0
    l = [0]
    for i in range(len(a)):
        s += a[i]
        l.append(s)
    return max(l)
