Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if P[i] == X:
            print(i+1)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if P[i] == X:
            print(i+1)
            break

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    print(P.index(X)+1)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    print(p.index(x) + 1)

=======
Suggestion 5

def main():
    # 入力
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    # 処理
    for i in range(n):
        if p[i] == x:
            ans = i + 1
    # 出力
    print(ans)
