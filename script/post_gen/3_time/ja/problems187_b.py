Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if y[i] - y[j] <= (x[i] - x[j]) * 1 and y[i] - y[j] >= (x[i] - x[j]) * (-1):
                count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (xy[j][1]-xy[i][1]) / (xy[j][0]-xy[i][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                count += 1

    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) <= 1:
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    points.sort()
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (points[j][1] - points[i][1]) * 2 <= points[j][0] - points[i][0]:
                count += 1
    print(count)

main()

=======
Suggestion 9

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    #print(points)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (points[i][1]-points[j][1])/(points[i][0]-points[j][0]) <= 1:
                cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    N = int(input())
    #N個の点の座標を格納するリスト
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append([x, y])
    #print(points)
    #傾きを計算する
    #傾きが-1以上1以下の組み合わせの個数を求める
    #傾きが-1以上1以下であれば、傾きの分母は正である
    #傾きの分母が正の場合、分子が正の組み合わせの個数を求める
    #分子が正の場合、分子の絶対値が分母より小さい
    #分子の絶対値が分母より小さい場合、分子の絶対値を分母で割った値が傾きの絶対値になる
    #傾きの絶対値が1以下であれば、傾きが-1以上1以下である
    #傾きが-1以上1以下であれば、分子の絶対値が分母より小さい
    #分子の絶対値が分母より小さい場合、分子の絶対値を分母で割った値が傾きの絶対値になる
    #分子の絶対値を分母で割った値が傾きの絶対値になる場合、分子の絶対値が分母より小さい
    #分子の絶対値が分母より小さい場合、分子の絶対値を分母で割った値が傾きの絶対値になる
