Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(1, N+1):
        D.append(D[i-1]+L[i-1])
    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 0
    for d in D:
        if d <= X:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 0
    for i in range(N+1):
        if D[i] <= X:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([i for i in D if i <= X]))

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([d for d in D if d <= X]))

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    count = 0
    for i in range(N):
        if D[i] + L[i] <= X:
            D.append(D[i] + L[i])
            count += 1
        else:
            break
    print(count + 1)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    #print(N, X)
    #print(L)

    #数直線の座標がX以下の領域でボールが跳ねる回数
    #ボールは順に座標 0, 3, 7, 12 で跳ねるので、座標 6 以下の領域で跳ねる回数は 2 回です。
    #ボールは順に座標 0, 3, 6, 9, 12 で跳ねるので、座標 9 以下の領域で跳ねる回数は 4 回です。

    #数直線の座標がX以下の領域でボールが跳ねる回数
    #ボールは順に座標 0, 3, 7, 12 で跳ねるので、座標 6 以下の領域で跳ねる回数は 2 回です。
    #ボールは順に座標 0, 3, 6, 9, 12 で跳ねるので、座標 9 以下の領域で跳ねる回数は 4 回です。

    #数直線の座標がX以下の領域でボールが跳ねる回数
    #ボールは順に座標 0, 3, 7, 12 で跳ねるので、座標 6 以下の領域で跳ねる回数は 2 回です。
    #ボールは順に座標 0, 3, 6, 9, 12 で跳ねる

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    # 座標を格納するリスト
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])

    # 答えを格納する変数
    ans = 0
    for i in range(N + 1):
        if D[i] <= X:
            ans += 1

    print(ans)
