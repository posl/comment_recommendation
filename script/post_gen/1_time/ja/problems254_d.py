Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j <= N:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N:
                cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i * j <= n:
                count += 1
            else:
                break
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        ans += N//i - i + 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j <= n:
                if i == j:
                    ans += 1
                else:
                    ans += 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        ans += (N // i - i + 1)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    # N = 254
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N:
                count += 1
    print(count)

=======
Suggestion 8

def main():
    # 入力
    N = int(input())
    # 処理
    i = 1
    cnt = 0
    while i * i <= N:
        j = 1
        while i * j <= N:
            cnt += 1
            j += 1
        i += 1
    # 出力
    print(cnt)
