Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n, d = map(int, input().split())
    x_list = []
    y_list = []
    for i in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)

    cnt = 0
    for i in range(n):
        if x_list[i]**2 + y_list[i]**2 <= d**2:
            cnt += 1
    print(cnt)

main()

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if (X**2 + Y**2)**(1/2) <= D:
            count += 1
    print(count)

=======
Suggestion 4

def solve():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x ** 2 + y ** 2 <= D ** 2:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def solve():
    N,D = map(int,input().split())
    ans = 0
    for _ in range(N):
        x,y = map(int,input().split())
        if x**2+y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n,d = map(int,input().split())
    x = []
    y = []
    for i in range(n):
        xi,yi = map(int,input().split())
        x.append(xi)
        y.append(yi)
    count = 0
    for i in range(n):
        if x[i]**2 + y[i]**2 <= d**2:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    x = []
    y = []
    for _ in range(n):
        tmp_x, tmp_y = map(int, input().split())
        x.append(tmp_x)
        y.append(tmp_y)
    cnt = 0
    for i in range(n):
        if x[i]**2 + y[i]**2 <= d**2:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def calc_distance(x,y):
    return (x**2+y**2)**(1/2)

n,d = map(int,input().split())
count = 0
for i in range(n):
    x,y = map(int,input().split())
    if calc_distance(x,y) <= d:
        count += 1

print(count)

=======
Suggestion 9

def main():
    # 標準入力の取得
    n, d = map(int, input().split())
    # 点の数
    #print(n)
    # 原点からの距離
    #print(d)

    # 座標のリスト
    point_list = []
    for i in range(n):
        x, y = map(int, input().split())
        point_list.append([x, y])
    #print(point_list)

    # 原点からの距離が d 以下の点の個数
    count = 0
    for point in point_list:
        if (point[0]**2 + point[1]**2)**(1/2) <= d:
            count += 1
    print(count)
