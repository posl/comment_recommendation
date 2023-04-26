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
    print(P.index(X) + 1)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    print(p.index(x) + 1)

=======
Suggestion 5

def main():
    #input
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    #output
    print(P.index(X)+1)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))

    # P = (2,3,1,4) なので、P_2 = 3 です。したがって、2 を出力します。
    # P = (3,5,1,4,2) なので、P_5 = 2 です。したがって、5 を出力します。
    # P = (1,2,3,4,5,6) なので、P_6 = 6 です。したがって、6 を出力します。

    # p.index(x) で、x のインデックスを取得
    print(p.index(x) + 1)
