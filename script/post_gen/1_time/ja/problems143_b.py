Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += d[i] * d[j]
    print(ans)

main()

=======
Suggestion 3

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += d[i]*d[j]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += d[i]*d[j]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    d = [int(i) for i in input().split()]
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 6

def main():
    # input
    N = int(input())
    ds = list(map(int, input().split()))

    # compute
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += ds[i] * ds[j]

    # output
    print(ans)

=======
Suggestion 7

def main():
    # 入力
    N = int(input())
    d = list(map(int, input().split()))
    # 処理
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += d[i] * d[j]
    # 出力
    print(ans)

=======
Suggestion 8

def main():
    # 入力
    N = int(input())
    d = list(map(int, input().split()))
    # 出力
    ans = 0
    for i in range(0, N):
        for j in range(i + 1, N):
            ans += d[i] * d[j]
    print(ans)
