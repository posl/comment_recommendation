Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    #print(x, y)
    #print(N)

    # リストの要素を全て入れ替える
    import itertools
    l = list(itertools.permutations(range(N)))
    #print(l)

    # 距離を求める関数
    def distance(i, j):
        return ( (x[i]-x[j])**2 + (y[i]-y[j])**2 )**0.5

    # 距離の合計を求める
    sum = 0
    for i in l:
        for j in range(N-1):
            sum += distance(i[j], i[j+1])
    #print(sum)

    # 平均を求める
    average = sum / len(l)
    print(average)

=======
Suggestion 2

def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    # 順列を列挙する
    import itertools
    order = list(itertools.permutations(range(N)))
    
    # 経路の長さの総和
    total = 0
    for o in order:
        for i in range(N-1):
            x1, y1 = X[o[i]], Y[o[i]]
            x2, y2 = X[o[i+1]], Y[o[i+1]]
            total += ((x1-x2)**2+(y1-y2)**2)**0.5
    
    # 平均
    ave = total / len(order)
    print(ave)

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    print(x)
    print(y)

=======
Suggestion 4

def main():
    import sys
    import itertools
    import math
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for p in itertools.permutations(range(N)):
        for i in range(N-1):
            ans += math.sqrt((x[p[i]]-x[p[i+1]])**2 + (y[p[i]]-y[p[i+1]])**2)
    ans /= math.factorial(N)
    print(ans)

=======
Suggestion 5

def main():
    import sys
    from itertools import permutations
    input = sys.stdin.readline
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    d = 0
    for p in permutations(range(N)):
        for i in range(N-1):
            d += ((XY[p[i]][0]-XY[p[i+1]][0])**2+(XY[p[i]][1]-XY[p[i+1]][1])**2)**0.5
    print(d/N)

=======
Suggestion 6

def main():
    import sys
    import math
    import itertools
    N = int(sys.stdin.readline())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, sys.stdin.readline().split())
        x.append(x_i)
        y.append(y_i)
    xy = list(itertools.permutations(range(N)))
    ans = 0
    for i in xy:
        for j in range(N-1):
            ans += math.sqrt((x[i[j]]-x[i[j+1]])**2+(y[i[j]]-y[i[j+1]])**2)
    print(ans/len(xy))

=======
Suggestion 7

def main():
    import itertools
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]

    # 全ての経路の長さの合計を求める
    ans = 0
    for p in itertools.permutations(range(N)):
        for i in range(N-1):
            ans += ((xy[p[i]][0]-xy[p[i+1]][0])**2+(xy[p[i]][1]-xy[p[i+1]][1])**2)**0.5
    # N!で割る
    ans /= math.factorial(N)

    print(ans)

=======
Suggestion 8

def main():
    import sys
    import math
    import itertools
    N = int(sys.stdin.readline())
    xy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    #print(xy)
    #print(len(xy))
    #print(xy[0][0])
    #print(xy[0][1])
    #print(xy[1][0])
    #print(xy[1][1])
    #print(xy[2][0])
    #print(xy[2][1])
    #print(xy[3][0])
    #print(xy[3][1])
    #print(xy[4][0])
    #print(xy[4][1])
    #print(xy[5][0])
    #print(xy[5][1])
    #print(xy[6][0])
    #print(xy[6][1])
    #print(xy[7][0])
    #print(xy[7][1])
    #print(xy[8][0])
    #print(xy[8][1])
    #print(xy[9][0])
    #print(xy[9][1])
    #print(xy[10][0])
    #print(xy[10][1])
    #print(xy[11][0])
    #print(xy[11][1])
    #print(xy[12][0])
    #print(xy[12][1])
    #print(xy[13][0])
    #print(xy[13][1])
    #print(xy[14][0])
    #print(xy[14][1])
    #print(xy[15][0])
    #print(xy[15][1])
    #print(xy[16][0])
    #print(xy[16][1])
    #print(xy[17][0])
    #print(xy[17][1])
    #print(xy[18][0])
    #print(xy[18][1])
    #print(xy[19][0])
    #print(xy[19][1])
    #print(xy[20][0])
    #print(xy[20][1])
    #print(xy[21][0])
    #print(xy[21][1])
    #print(xy[22][0])
    #print(xy[22][1])
    #print(xy[23][0])
    #print(xy[23][1])
    #print(xy[24][0])
    #print(xy[24

=======
Suggestion 9

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]

    # 1からNまでの順列を列挙
    import itertools
    p = itertools.permutations(range(N))

    # 順列の組み合わせを全て計算
    import math
    ans = 0
    for i in p:
        for j in range(N-1):
            ans += math.sqrt((xy[i[j]][0]-xy[i[j+1]][0])**2 + (xy[i[j]][1]-xy[i[j+1]][1])**2)
    print(ans/math.factorial(N))
