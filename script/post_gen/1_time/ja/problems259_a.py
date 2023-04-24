Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, X, T, D = map(int, input().split())
    if M >= X:
        print(T + (N - M) * D)
    else:
        print(T + (X - M) * D)

=======
Suggestion 2

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + (N - X) * D)
    else:
        print(T)

main()

=======
Suggestion 3

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + D * (M - X))
    else:
        print(T)

=======
Suggestion 4

def main():
    N, M, X, T, D = map(int, input().split())
    if N <= X:
        print(T + D * (N - 1))
    else:
        print(T + D * (X - 1) + (N - X))

=======
Suggestion 5

def main():
    N, M, X, T, D = map(int, input().split())
    if M >= X:
        print(T + D*(M-X))
    else:
        print(T + D*(N-X))

=======
Suggestion 6

def main():
    n, m, x, t, d = map(int, input().split())
    if m < x:
        t += d * (m - x)
    print(t)

=======
Suggestion 7

def main():
    #input
    N, M, X, T, D = map(int, input().split())

    #compute
    if M < X:
        ans = T + (N-X)*D
    else:
        ans = T - (M-X)*D

    #output
    print(ans)

=======
Suggestion 8

def main():
    N, M, X, T, D = map(int, input().split())
    if M == 0:
        print(T - X * D)
    else:
        print(T)

=======
Suggestion 9

def main():
    #入力
    N, M, X, T, D = map(int, input().split())
    #M歳の誕生日の時の身長を求める
    H = T + D * (M - X)
    #M歳の誕生日の時の身長がN歳の誕生日の時の身長よりも低い場合、
    #N歳の誕生日の時の身長を出力する
    if H < T + D * (N - X):
        print(T + D * (N - X))
    #M歳の誕生日の時の身長がN歳の誕生日の時の身長よりも高い場合、
    #M歳の誕生日の時の身長を出力する
    else:
        print(H)
