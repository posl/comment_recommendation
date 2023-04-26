Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for s in S:
        ans += T.count(s[-3:])
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    ans = 0
    for s in S:
        ans += sum(s[-3:] == t for t in T)

    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        if s[i][3:] in t:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for t in T:
        print(S.count(t))

=======
Suggestion 5

def main():
    # 入力
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    T = []
    for i in range(M):
        T.append(input())
    # 処理
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
    # 出力
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    for i in range(N):
        cnt = 0
        for j in range(M):
            if S[i][-3:] == T[j]:
                cnt += 1
        print(cnt)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    print(sum([S[i][-3:] in T for i in range(N)]))

=======
Suggestion 8

def main():
    #入力
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    #処理
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1

    #出力
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    #print(N, M)
    #print(S)
    #print(T)

    # 末尾3文字が一致するものの数をカウント
    cnt = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    for i in range(n):
        cnt = 0
        for j in range(m):
            if s[i][-3:] == t[j]:
                cnt += 1
        print(cnt)
