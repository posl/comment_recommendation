Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    X = 0
    Y = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            X += V[i]
            Y += C[i]
    print(X - Y)

=======
Suggestion 2

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    X = 0
    Y = 0
    for i in range(N):
        if V[i] > C[i]:
            X += V[i]
            Y += C[i]
    print(X-Y)

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += v[i] - c[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    x = 0
    y = 0
    for i in range(n):
        if v[i] > c[i]:
            x += v[i]
            y += c[i]

    print(x-y)

=======
Suggestion 6

def main():
    n = int(input())
    v = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += v[i] - c[i]
    print(ans)

main()

=======
Suggestion 7

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    max = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            max += V[i] - C[i]
    print(max)

=======
Suggestion 8

def main():
    n = int(input())
    v_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))

    x_y_list = [v_list[i] - c_list[i] for i in range(n)]
    x_y_list.sort(reverse=True)

    print(sum([x_y_list[i] for i in range(n) if x_y_list[i] > 0]))

=======
Suggestion 9

def main():
    # 標準入力受付
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # 価値の合計
    X = 0
    # 支払いコストの合計
    Y = 0
    # X-Yの最大値
    max = 0

    # 宝石の数だけループ
    for i in range(N):
        # 価値の合計に宝石の価値を加算
        X += V[i]
        # 支払いコストの合計に宝石の支払いコストを加算
        Y += C[i]
        # X-Yの最大値を更新
        if max < X-Y:
            max = X-Y

    # X-Yの最大値を出力
    print(max)
