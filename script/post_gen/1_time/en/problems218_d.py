Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += (X[j]-X[i])*(Y[j]-Y[i])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            for k in range(j + 1, n):
                if x[i] == x[k] or y[i] == y[k]:
                    continue
                if x[i] == x[j] or y[i] == y[j]:
                    continue
                if (x[i] - x[j]) * (y[i] - y[k]) == (x[i] - x[k]) * (y[i] - y[j]):
                    count += 1
    print(count)

main()

=======
Suggestion 3

def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    x.sort()
    y.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += (x[j]-x[i])*(y[j]-y[i])
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x = sorted(x)
    y = sorted(y)
    xcount = [0] * (10 ** 9 + 1)
    ycount = [0] * (10 ** 9 + 1)
    for i in range(n):
        xcount[x[i]] += 1
        ycount[y[i]] += 1
    xsum = [0] * (10 ** 9 + 1)
    ysum = [0] * (10 ** 9 + 1)
    for i in range(1, 10 ** 9 + 1):
        xsum[i] = xsum[i - 1] + xcount[i]
        ysum[i] = ysum[i - 1] + ycount[i]
    ans = 0
    for i in range(n):
        ans += (xsum[x[i] - 1]) * (n - xsum[x[i]])
        ans += (ysum[y[i] - 1]) * (n - ysum[y[i]])
    print(ans // 2)

=======
Suggestion 5

def solve():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X = sorted(X)
    Y = sorted(Y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += (X[j]-X[i]) * (Y[j]-Y[i])
    print(ans)

=======
Suggestion 6

def main():
    from collections import Counter
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    
    c = Counter()
    for i in range(N):
        for j in range(i + 1, N):
            c[(x[i] + x[j], y[i] + y[j])] += 1
    
    ans = 0
    for k, v in c.items():
        ans += v * (v - 1) // 2
    
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    x_y = []
    for _ in range(N):
        x, y = map(int, input().split())
        x_y.append((x, y))

    x_y.sort(key=lambda x: x[0])
    x = [x_y[i][0] for i in range(N)]
    y = [x_y[i][1] for i in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    if x[i] == x[j] and y[k] == y[l]:
                        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    points.sort(key=lambda x: x[0])
    result = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            count = 0
            for k in range(N):
                if points[i][0] <= points[k][0] <= points[j][0] and points[i][1] <= points[k][1] <= points[j][1]:
                    count += 1
            result += count * (count - 1) // 2
    print(result)

main()

=======
Suggestion 9

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    # x座標を基準にソート
    points.sort(key=lambda x: x[0])

    # x座標が同じものをグループ化
    x_group = []
    tmp = []
    for i in range(N):
        if i == 0:
            tmp.append(points[0])
        else:
            if points[i][0] == points[i - 1][0]:
                tmp.append(points[i])
            else:
                x_group.append(tmp)
                tmp = []
                tmp.append(points[i])
    x_group.append(tmp)

    # y座標を基準にソート
    for i in range(len(x_group)):
        x_group[i].sort(key=lambda x: x[1])

    # y座標が同じものをグループ化
    y_group = []
    for i in range(len(x_group)):
        tmp = []
        for j in range(len(x_group[i])):
            if j == 0:
                tmp.append(x_group[i][0])
            else:
                if x_group[i][j][1] == x_group[i][j - 1][1]:
                    tmp.append(x_group[i][j])
                else:
                    y_group.append(tmp)
                    tmp = []
                    tmp.append(x_group[i][j])
        y_group.append(tmp)

    # それぞれのグループの中から2点を選ぶ組み合わせを求める
    ans = 0
    for i in range(len(y_group)):
        ans += (len(y_group[i]) * (len(y_group[i]) - 1)) // 2

    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    points.sort(key=lambda x:(x[0],x[1]))
    x_dic = {}
    y_dic = {}
    for i in range(N):
        if points[i][0] in x_dic:
            x_dic[points[i][0]].append(points[i][1])
        else:
            x_dic[points[i][0]] = [points[i][1]]
        if points[i][1] in y_dic:
            y_dic[points[i][1]].append(points[i][0])
        else:
            y_dic[points[i][1]] = [points[i][0]]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if points[i][0] == points[j][0]:
                continue
            if points[i][1] == points[j][1]:
                continue
            if points[i][1] in y_dic[points[j][1]]:
                if points[i][0] in x_dic[points[j][0]]:
                    ans += 1
    print(ans)
