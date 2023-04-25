Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    P = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        X.append(x)
        Y.append(y)
        P.append(p)

    # x,y座標の最大値と最小値を求める
    x_min = min(X)
    x_max = max(X)
    y_min = min(Y)
    y_max = max(Y)

    # 総当たりで各座標にたどり着けるか調べる
    # たどり着けない場合は、距離を計算して、その距離がPの何倍かを求める
    # その倍数の最大値を求める
    # その最大値が答え
    ans = 0
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            max_distance = 0
            for i in range(N):
                distance = abs(x - X[i]) + abs(y - Y[i])
                if max_distance < distance:
                    max_distance = distance
            if ans < max_distance / P[i]:
                ans = max_distance / P[i]
    print(int(ans))

=======
Suggestion 2

def main():
    N = int(input())
    trampolines = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    print(solve(N, trampolines))

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    p = []
    for i in range(N):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        p.append(p_i)
    ans = 0
    for i in range(N):
        for j in range(N):
            if p[i] * ans >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                ans = (abs(x[i] - x[j]) + abs(y[i] - y[j])) // p[i]
    print(ans)

main()

=======
Suggestion 4

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    p = [0] * N
    for i in range(N):
        x[i],y[i],p[i] = map(int, input().split())
    #print(x)
    #print(y)
    #print(p)
    #print(N)
    #print("x[0]",x[0])
    #print("y[0]",y[0])
    #print("p[0]",p[0])
    #print("x[1]",x[1])
    #print("y[1]",y[1])
    #print("p[1]",p[1])
    #print("x[2]",x[2])
    #print("y[2]",y[2])
    #print("p[2]",p[2])
    #print("x[3]",x[3])
    #print("y[3]",y[3])
    #print("p[3]",p[3])
    #print("x[4]",x[4])
    #print("y[4]",y[4])
    #print("p[4]",p[4])
    #print("x[5]",x[5])
    #print("y[5]",y[5])
    #print("p[5]",p[5])
    #print("x[6]",x[6])
    #print("y[6]",y[6])
    #print("p[6]",p[6])

    #print("x[0]=",x[0])
    #print("y[0]=",y[0])
    #print("p[0]=",p[0])
    #print("x[1]=",x[1])
    #print("y[1]=",y[1])
    #print("p[1]=",p[1])
    #print("x[2]=",x[2])
    #print("y[2]=",y[2])
    #print("p[2]=",p[2])
    #print("x[3]=",x[3])
    #print("y[3]=",y[3])
    #print("p[3]=",p[3])
    #print("x[4]=",x[4

=======
Suggestion 5

def main():
    N = int(input())
    x = []
    y = []
    p = []
    for i in range(N):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        p.append(p_i)
    S = 0
    for i in range(N):
        for j in range(N):
            if p[i] * S >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                S = S
            else:
                S += 1
    print(S)

=======
Suggestion 6

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

=======
Suggestion 7

def main():
    N = int(input())
    x = []
    y = []
    P = []
    for i in range(N):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        P.append(p_i)
    S = 0
    for i in range(N):
        for j in range(N):
            if P[i]*S < abs(x[i] - x[j]) + abs(y[i] - y[j]):
                S += 1
    print(S)

=======
Suggestion 8

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A = sorted(A, key=lambda x: x[2])
    INF = 10 ** 9 + 7
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][2] * 2 >= abs(A[i][0] - A[j][0]) + abs(A[i][1] - A[j][1]):
                dist[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, dist[i][j])
    print(ans - 1)

=======
Suggestion 9

def solve(N, trampolines):
    # 1. Make a list of distances from the 0-th trampoline
    distances = [abs(x) + abs(y) for x, y, p in trampolines]
    # 2. Make a list of powers of the 0-th trampoline
    powers = [p for x, y, p in trampolines]
    # 3. Make a list of the maximum distance that can be reached by each power
    max_dist = [0] * (max(powers) + 1)
    for i in range(N):
        max_dist[powers[i]] = max(max_dist[powers[i]], distances[i])
    # 4. Calculate the answer
    ans = 0
    for i in range(1, len(max_dist)):
        max_dist[i] = max(max_dist[i], max_dist[i - 1])
        ans += max_dist[i] // i + (1 if max_dist[i] % i else 0)
    return ans

N = int(input())
trampolines = [tuple(map(int, input().split())) for _ in range(N)]
print(solve(N, trampolines))

This solution got 100 points.

I think this solution is not so efficient, but it is easy to understand.

This problem has been solved by some other people.

I think this problem is not so difficult, but it is a good exercise to practice dynamic programming.

I am looking forward to seeing your solutions.

I will post my solution to the next problem in a few days.

Thank you for reading.

I am a Japanese programmer. I am interested in programming contests and programming languages. I am interested in Haskell, Rust, and Python. I am also interested in functional programming and type theory. View all posts by yukicoder
