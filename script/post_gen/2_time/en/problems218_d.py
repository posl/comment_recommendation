Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    x_count = {}
    y_count = {}
    for i in range(N):
        if X[i] in x_count:
            x_count[X[i]] += 1
        else:
            x_count[X[i]] = 1
        if Y[i] in y_count:
            y_count[Y[i]] += 1
        else:
            y_count[Y[i]] = 1
    x_sum = 0
    y_sum = 0
    for i in range(N):
        x_sum += x_count[X[i]] - 1
        y_sum += y_count[Y[i]] - 1
    print(x_sum * y_sum)

=======
Suggestion 2

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    #print(x)
    #print(y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if x[i] == x[j]:
                    if y[i] == y[k] or y[j] == y[k]:
                        ans += 1
                elif x[i] == x[k]:
                    if y[i] == y[j] or y[j] == y[k]:
                        ans += 1
                elif x[j] == x[k]:
                    if y[i] == y[j] or y[i] == y[k]:
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
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if x[i] == x[j]:
                for k in range(j+1, N):
                    if y[i] == y[k]:
                        for l in range(k+1, N):
                            if y[j] == y[l]:
                                ans += 1
            elif y[i] == y[j]:
                for k in range(j+1, N):
                    if x[i] == x[k]:
                        for l in range(k+1, N):
                            if x[j] == x[l]:
                                ans += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            x = X[j] - X[i]
            for k in range(N-1):
                for l in range(k+1,N):
                    y = Y[l] - Y[k]
                    if x*y == 0:
                        continue
                    if (X[i],Y[k]) in zip(X,Y) and (X[j],Y[l]) in zip(X,Y):
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
    x.sort()
    y.sort()
    x_num = []
    y_num = []
    x_num.append(1)
    y_num.append(1)
    for i in range(N-1):
        if x[i] == x[i+1]:
            x_num[-1] += 1
        elif x[i] != x[i+1]:
            x_num.append(1)
        if y[i] == y[i+1]:
            y_num[-1] += 1
        elif y[i] != y[i+1]:
            y_num.append(1)
    x_num.sort(reverse=True)
    y_num.sort(reverse=True)
    x_ans = 0
    y_ans = 0
    for i in range(len(x_num)):
        x_ans += x_num[i] * (i + 1)
    for i in range(len(y_num)):
        y_ans += y_num[i] * (i + 1)
    print(x_ans * y_ans)

=======
Suggestion 6

def main():
    from collections import Counter
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    x_count = Counter(x)
    y_count = Counter(y)
    x_count = list(x_count.values())
    y_count = list(y_count.values())
    ans = 0
    for i in range(len(x_count)):
        for j in range(len(x_count)):
            if i == j:
                ans += x_count[i] * (x_count[j] - 1) // 2
            else:
                ans += x_count[i] * x_count[j]
    for i in range(len(y_count)):
        for j in range(len(y_count)):
            if i == j:
                ans += y_count[i] * (y_count[j] - 1) // 2
            else:
                ans += y_count[i] * y_count[j]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    P = []
    for i in range(N):
        x,y = map(int,input().split())
        P.append([x,y])
    P.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (P[k][1] - P[i][1])*(P[j][0] - P[i][0]) == (P[j][1] - P[i][1])*(P[k][0] - P[i][0]):
                    ans += 1
    print(ans)

main()

=======
Suggestion 8

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    #print(points)

    #x, yの座標をそれぞれソート
    x_points = sorted(points, key=lambda x: x[0])
    y_points = sorted(points, key=lambda x: x[1])
    #print(x_points)
    #print(y_points)

    #x, yの座標のリストを作る
    x_list = []
    y_list = []
    for i in range(N):
        x_list.append(x_points[i][0])
        y_list.append(y_points[i][1])
    #print(x_list)
    #print(y_list)

    #x, yの座標のリストから、重複を削除したリストを作る
    x_list2 = list(set(x_list))
    y_list2 = list(set(y_list))
    #print(x_list2)
    #print(y_list2)

    #x, yの座標のリストから、重複を削除したリストの長さを取得
    x_len = len(x_list2)
    y_len = len(y_list2)
    #print(x_len)
    #print(y_len)

    #x, yの座標のリストから、重複を削除したリストの長さを取得
    x_len = len(x_list2)
    y_len = len(y_list2)
    #print(x_len)
    #print(y_len)

    #x, yの座標のリストから、重複を削除したリストの長さを取得
    x_len = len(x_list2)
    y_len = len(y_list2)
    #print(x_len)
    #print(y_len)

    #x, yの座標のリストから、重複を削除したリストの長さを取得
    x_len = len(x_list2)
    y_len = len(y_list2)
    #print(x_len)
    #print(y

=======
Suggestion 9

def main():
    N = int(input())
    x_y = []
    for i in range(N):
        a,b = map(int,input().split())
        x_y.append([a,b])
    x_y.sort()
    x = []
    y = []
    for i in range(N):
        x.append(x_y[i][0])
        y.append(x_y[i][1])
    x_count = []
    y_count = []
    x_count.append(1)
    y_count.append(1)
    for i in range(1,N):
        if x[i] == x[i-1]:
            x_count.append(x_count[i-1]+1)
        else:
            x_count.append(1)
        if y[i] == y[i-1]:
            y_count.append(y_count[i-1]+1)
        else:
            y_count.append(1)
    ans = 0
    for i in range(N):
        ans += x_count[i]*(x_count[i]-1)//2
        ans += y_count[i]*(y_count[i]-1)//2
    print(ans)

main()

問題文

N 個の整数 a_1,a_2,...,a_N が与えられます。a_1,a_2,...,a_N を 1 つ以上選んで、その和をとったときの和の最大値を求めてください。

制約
1 ≦ N ≦ 20
-10^9 ≦ a_i ≦ 10^9
入力はすべて整数である。
入力は全て 0 であることもありえる。

入力
入力は以下の形式で標準入力から与えられる。
N
a_1 a_2 ... a_N

出力
a_1,a_2,...,a_N を 1 つ以上選んで、その和をとったときの和の最大値を出力せよ。

入力例 1
4
-2 1 -4 3

出力例 1
4

入力例 2
5
-5 -3 -1 2 4

出力例 2
6

入力例 3
5
-1 -
