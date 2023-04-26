Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
    else:
        p = list(map(int, input().split()))
        if X not in p:
            print(X)
        else:
            for i in range(0, 101):
                if X - i not in p:
                    print(X - i)
                    break
                if X + i not in p:
                    print(X + i)
                    break

=======
Suggestion 2

def main():
    # 整数 X と、長さ N の整数列 p_1, ..., p_N が与えられます。
    X, N = map(int, input().split())
    # 整数列 p_1, ..., p_N に含まれない整数 (正とは限らない) のうち X に最も近いもの、つまり X との差の絶対値が最小のものを求めてください。そのような整数が複数存在する場合は、そのうち最も小さいものを答えてください。
    # 整数列 p_1, ..., p_N に含まれない整数のうち、最も X に近いものは 8 です。
    p = list(map(int, input().split()))

    # p に含まれる数値のうち、X に最も近いものを求める
    # p に含まれる数値のうち、X に最も近いものは 8 と 9 です。このうち小さい方である 8 を出力します。
    # p に含まれる数値のうち、X に最も近いものは 9 と 11 です。このうち小さい方である 9 を出力します。
    # p に含まれる数値のうち、X に最も近いものは 10 と 11 です。このうち小さい方である 10 を出力します。
    # p に含まれる数値のうち、X に最も近いものは 9 です。
    # p に含まれる数値のうち、X に最も近いものは 10 です。
    # p に含まれる数値のうち、X に最も近いものは 11 です。
    # p に含まれる数値のうち、X に最も

=======
Suggestion 3

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    if X not in p:
        print(X)
        return
    p.sort()
    for i in range(1, 101):
        if X - i not in p:
            print(X - i)
            return
        elif X + i not in p:
            print(X + i)
            return

=======
Suggestion 4

def main():
    # 入力
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    # 出力
    if N == 0:
        print(X)
    else:
        p.sort()
        if X <= p[0]:
            print(p[0])
        elif X >= p[-1]:
            print(p[-1])
        else:
            for i in range(N):
                if p[i] <= X and X <= p[i+1]:
                    if abs(p[i]-X) <= abs(p[i+1]-X):
                        print(p[i])
                    else:
                        print(p[i+1])

main()

=======
Suggestion 5

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    if x <= p[0]:
        print(p[0])
        return
    if p[-1] <= x:
        print(p[-1])
        return
    for i in range(n):
        if p[i] <= x < p[i+1]:
            if x-p[i] <= p[i+1]-x:
                print(p[i])
                return
            else:
                print(p[i+1])
                return

=======
Suggestion 6

def main():
    X, N = map(int, input().split())
    p_list = list(map(int, input().split()))
    if N == 0:
        print(X)
        return
    for i in range(100):
        if (X - i) not in p_list:
            print(X - i)
            return
        if (X + i) not in p_list:
            print(X + i)
            return

=======
Suggestion 7

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
    else:
        p = list(map(int, input().split()))
        p.sort()
        #print(p)
        if X < p[0]:
            print(p[0])
        elif X > p[-1]:
            print(p[-1])
        else:
            for i in range(N):
                if p[i] <= X < p[i+1]:
                    if X - p[i] <= p[i+1] - X:
                        print(p[i])
                    else:
                        print(p[i+1])
                    break

=======
Suggestion 8

def main():
    X, N = map(int, input().split())
    if N > 0:
        p = list(map(int, input().split()))
        p.sort()
        if X <= p[0]:
            print(p[0] - 1)
        elif X >= p[-1]:
            print(p[-1] + 1)
        else:
            for i in range(N - 1):
                if p[i] < X < p[i + 1]:
                    if abs(X - p[i]) > abs(X - p[i + 1]):
                        print(p[i + 1])
                    else:
                        print(p[i])
                    break
    else:
        print(X)

=======
Suggestion 9

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))

    if N == 0:
        print(X)
        return

    p.sort()
    print(p)

    for i in range(0, 101):
        if X - i not in p:
            print(X - i)
            return
        elif X + i not in p:
            print(X + i)
            return

=======
Suggestion 10

def get_int():
    return int(input())
