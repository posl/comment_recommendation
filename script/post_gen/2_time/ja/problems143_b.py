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
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 4

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
