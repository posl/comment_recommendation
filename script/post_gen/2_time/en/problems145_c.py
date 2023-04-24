Synthesizing 10/10 solutions

=======
Suggestion 1

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 2

def main():
    import itertools
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in itertools.permutations(range(n)):
        for j in range(n-1):
            ans += ((x[i[j]] - x[i[j+1]])**2 + (y[i[j]] - y[i[j+1]])**2)**0.5
    print(ans / math.factorial(n))

=======
Suggestion 3

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    # print(X)
    # print(Y)
    # print(N)
    # print(math.factorial(N))
    # print(2**N)
    # print(N**N)
    # print(N**2)
    # print(N**3)
    # print(N**4)
    # print(N**5)
    # print(N**6)
    # print(N**7)
    # print(N**8)

    # print(2**N)
    # print(N**N)
    # print(N**2)
    # print(N**3)
    # print(N**4)
    # print(N**5)
    # print(N**6)
    # print(N**7)
    # print(N**8)

    # print(2**N)
    # print(N**N)
    # print(N**2)
    # print(N**3)
    # print(N**4)
    # print(N**5)
    # print(N**6)
    # print(N**7)
    # print(N**8)

    # print(2**N)
    # print(N**N)
    # print(N**2)
    # print(N**3)
    # print(N**4)
    # print(N**5)
    # print(N**6)
    # print(N**7)
    # print(N**8)

    # print(2**N)
    # print(N**N)
    # print(N**2)
    # print(N**3)
    # print(N**4)
    # print(N**5)
    # print(N**6)
    # print(N**7)
    # print(N**8)

    # print(2**N)
    # print(N**N)
    # print(N**2)
    # print(N**3)
    # print(N**4)
    # print(N**5)
    # print(N**6)
    # print(N**7)
    # print(N**8)

    # print(2**N)
    # print(N**N)
    # print(N**2)
    # print(N**3)
    # print(N**4)
    # print(N**5)
    # print(N**

=======
Suggestion 4

def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += ((XY[i][0]-XY[j][0])**2+(XY[i][1]-XY[j][1])**2)**0.5
    print(ans*2/N)

=======
Suggestion 5

def calc_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 6

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x0,y0 = map(int,input().split())
        x.append(x0)
        y.append(y0)
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            ans += ((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
    print(ans*2/N)

=======
Suggestion 7

def main():
    from itertools import permutations
    import math
    N = int(input())
    towns = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in permutations(range(N)):
        for i in range(N-1):
            ans += math.sqrt((towns[p[i]][0]-towns[p[i+1]][0])**2 + (towns[p[i]][1]-towns[p[i+1]][1])**2)
    print(ans/math.factorial(N))

=======
Suggestion 8

def solve():
    N = int(input())
    x_y = [list(map(int, input().split())) for _ in range(N)]
    from itertools import permutations
    from math import sqrt
    ans = 0
    for p in permutations(range(N)):
        for i in range(N-1):
            ans += sqrt((x_y[p[i]][0]-x_y[p[i+1]][0])**2 + (x_y[p[i]][1]-x_y[p[i+1]][1])**2)
    print(ans/len(list(permutations(range(N)))))

=======
Suggestion 9

def main():
    N = int(input())
    X = [tuple(map(int, input().split())) for _ in range(N)]
    X.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += ((X[i][0] - X[j][0]) ** 2 + (X[i][1] - X[j][1]) ** 2) ** 0.5
    print(ans * 2 / N / (N - 1))

main()

=======
Suggestion 10

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    #print(xy)

    #N!通りのパターンを作る
    import itertools
    pattern = list(itertools.permutations(range(N), N))
    #print(pattern)

    #パターンの長さを求める
    length = []
    for i in range(len(pattern)):
        l = 0
        for j in range(N-1):
            l += ((xy[pattern[i][j]][0]-xy[pattern[i][j+1]][0])**2+(xy[pattern[i][j]][1]-xy[pattern[i][j+1]][1])**2)**(1/2)
        length.append(l)
    #print(length)

    #平均を求める
    ave = sum(length)/len(pattern)
    print(ave)
