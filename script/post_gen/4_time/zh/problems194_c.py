Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += (n - i - 1) * a[i] ** 2
        sum -= (n - i - 1) * a[i] * 2 * sum
    print(sum)

=======
Suggestion 3

def main():
    #输入
    n = int(input())
    a = list(map(int, input().split()))

    #计算
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2

    #输出
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # ここにコードを書く
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (N - i) * (A[i] ** 2)
        ans -= 2 * A[i] * sum(A[:i])
        ans += sum(A[:i]) ** 2
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n,a)
    ans = 0
    for i in range(1,n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    print(ans)
