Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for a in range(1, N):
        for b in range(1, N):
            if a * b + b >= N:
                break
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for A in range(1, N):
        for B in range(1, N):
            C = N - (A * B)
            if C < 1:
                break
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        for j in range(1, N):
            if i*j + i + j == N:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    cnt = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a * b + b >= N:
                break
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        count += (N - 1) // i
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for A in range(1, N):
        for B in range(1, N):
            if A*B + B >= N:
                break
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for a in range(1, int(n**0.5)+1):
        for b in range(1, int(n**0.5)+1):
            c = a*b
            if c > n:
                break
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j + j == N:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    # 入力
    N = int(input())
    # 出力
    print(solve(N))

=======
Suggestion 10

def main():
    N = int(input()) #問題文の制約より、Nは2以上10^6以下の正整数
    ans = 0
    for i in range(1, N+1):
        ans += (N-1)//i
    print(ans)
