Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans += n-i-1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0 or A[i-1] != A[i]:
            ans += N - i - 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N - 1):
        ans += N - (i + 1) - (A[i] == A[i + 1])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    ans = 0
    for i in range(N-1):
        if A[i] != A[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    N = int(readline())
    A = list(map(int,readline().split()))
    if len(A) != N:
        print("入力エラー")
        return

    A.sort()
    ans = 0
    for i in range(N-1):
        ans += N - i - 1 - (A[i] == A[i+1])
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(set(A))
    B.sort()
    ans = 0
    for i in range(len(B)):
        ans += i
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (N - i) * (i + 1) - 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i - 1) - A[i] * (N - 1 - i)
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    #print(a)

    ans = 0
    for i in range(n):
        if i == n-1:
            break
        if a[i] == a[i+1]:
            continue
        ans += n-i-1
    print(ans)

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #ソート
    A.sort()
    #初期化
    ans = 0
    #ループ
    for i in range(N-1):
        if A[i] != A[i+1]:
            ans += (i+1)
    #出力
    print(ans)
