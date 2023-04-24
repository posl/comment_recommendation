Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    ans = 0
    for s in S:
        ans += s[-3:] in T

    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
                break
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())

    count = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                count += 1

    print(count)

=======
Suggestion 6

def main():
    #入力
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    #処理
    ans = 0
    for s in S:
        ans += sum([s[-3:] == t for t in T])
    #出力
    print(ans)

=======
Suggestion 7

def main():
    # 入力
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    # 出力
    for i in range(N):
        ans = 0
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
        print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]

    # print(N, M)
    # print(S)
    # print(T)

    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
                break

    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]

    print(sum(s.count(t[-3:]) for t in t))
