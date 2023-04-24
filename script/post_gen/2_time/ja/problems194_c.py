Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += (a[i] - a[j]) ** 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += (A[i]-A[j])**2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i - 1]) ** 2 * (i * (N - i))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i - 1]) ** 2 * i * (N - i)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (i * (A[i] - A[i - 1])) ** 2
    print(ans)

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #処理
    ans = 0
    for i in range(1,N):
        ans += (N-i)*A[i]**2 - 2*A[i]*sum(A[:i]) + i*A[i]**2
    #出力
    print(ans)
