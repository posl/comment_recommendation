Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 入力
    X, N = map(int, input().split())
    if N != 0:
        p = list(map(int, input().split()))
    else:
        p = []
    # 出力
    if N == 0:
        print(X)
    else:
        for i in range(101):
            if X-i not in p:
                print(X-i)
                break
            elif X+i not in p:
                print(X+i)
                break

=======
Suggestion 2

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    if N == 0:
        print(X)
    else:
        for i in range(100):
            if X - i not in p:
                print(X - i)
                break
            elif X + i not in p:
                print(X + i)
                break

=======
Suggestion 3

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    if N == 0:
        print(X)
        return
    p = sorted(p)
    for i in range(0, 101):
        if X - i not in p:
            print(X - i)
            return
        if X + i not in p:
            print(X + i)
            return

=======
Suggestion 4

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    p = set(p)
    for i in range(200):
        if X-i not in p:
            print(X-i)
            break
        if X+i not in p:
            print(X+i)
            break

=======
Suggestion 5

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    p.sort()
    #print(p)
    if X < p[0]:
        print(p[0])
        return
    elif X > p[-1]:
        print(p[-1])
        return
    else:
        for i in range(len(p)-1):
            if X > p[i] and X < p[i+1]:
                if X - p[i] > p[i+1] - X:
                    print(p[i+1])
                    return
                else:
                    print(p[i])
                    return

=======
Suggestion 6

def main():
    # input
    X, N = map(int, input().split())
    ps = [*map(int, input().split())] if N else []

    # compute
    for i in range(1000):
        if X-i not in ps:
            ans = X-i
            break
        if X+i not in ps:
            ans = X+i
            break

    # output
    print(ans)

=======
Suggestion 7

def main():
    X, N = map(int, input().split())
    P = list(map(int, input().split()))
    if N == 0:
        print(X)
        return
    P = list(set(P))
    P.sort()
    if X <= P[0]:
        print(P[0])
        return
    if X >= P[-1]:
        print(P[-1])
        return
    for i in range(N):
        if X <= P[i]:
            if X - P[i-1] <= P[i] - X:
                print(P[i-1])
                return
            else:
                print(P[i])
                return
main()

=======
Suggestion 8

def main():
    # 標準入力から X, N を取得
    X, N = map(int, input().split())
    # 標準入力から N 個の整数列 p を取得
    p = list(map(int, input().split()))
    # X との差の絶対値が最小のものを求める
    # 絶対値の最小値を 0 で初期化
    min_diff = 0
    # 絶対値の最小値になる数を X で初期化
    min_diff_num = X
    # X との差の絶対値が最小のものを求める
    for i in range(100):
        # X との差の絶対値を求める
        diff = abs(X - i)
        # 絶対値の最小値になる数を更新する
        if i not in p:
            if min_diff == 0:
                min_diff = diff
                min_diff_num = i
            elif min_diff > diff:
                min_diff = diff
                min_diff_num = i
    # 絶対値の最小値になる数を出力する
    print(min_diff_num)

=======
Suggestion 9

def main():
    # 1行目
    X, N = map(int, input().split())
    # 2行目
    p = list(map(int, input().split()))

    # 答え
    ans = 0

    # 答えを出力
    print(ans)

=======
Suggestion 10

def get_answer(X, N, p):
    if N == 0:
        return X
    else:
        i = 0
        while True:
            if X-i not in p:
                return X-i
            elif X+i not in p:
                return X+i
            else:
                i += 1
