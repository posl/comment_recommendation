Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        for j in range(i+1, n):
            if max < abs(a[i] - a[j]):
                max = abs(a[i] - a[j])
    print(max)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if ans < abs(A[i] - A[j]):
                ans = abs(A[i] - A[j])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1]-A[0])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1]-a[0])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1]-a[0])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(abs(max(a) - min(a)))

=======
Suggestion 8

def main():
    # 標準入力受け取り
    n = int(input())
    a = list(map(int, input().split()))
    # 絶対値の最大値を求める
    max = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(a[i]-a[j]) > max:
                max = abs(a[i]-a[j])
    # 標準出力
    print(max)
