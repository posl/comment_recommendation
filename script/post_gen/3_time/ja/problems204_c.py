Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(N*N - N - M)
    return

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(N)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = n * (n-1) // 2
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    g = [[0]*n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1][b-1] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                for k in range(n):
                    if g[j][k] == 1 and g[k][i] == 1:
                        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    print(N, M)
    for i in range(M):
        A, B = map(int, input().split())
        print(A, B)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    print(N * N - N * M - M * N + M * (M - 1) // 2)

=======
Suggestion 7

def comb(n,r):
    if r == 0:
        return 1
    else:
        return comb(n,r-1)*(n-r+1)//r

N,M = map(int,input().split())
print(comb(N,2) - M)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    print(n, m)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]

    #print(N,M)
    #print(AB)

    # 都市の組み合わせはN*(N-1)/2
    # それぞれの組み合わせに対して、スタート地点とゴール地点を決める
    # スタート地点とゴール地点の組み合わせが何通りあるかを計算する
    # 都市の組み合わせの数
    city_combination = int(N*(N-1)/2)
    # スタート地点とゴール地点の組み合わせの数
    start_goal_combination = 0
    for i in range(city_combination):
        for j in range(M):
            if i+1 == AB[j][0] or i+1 == AB[j][1]:
                #print(i+1,AB[j][0],AB[j][1])
                start_goal_combination += 1
                break
    #print(city_combination,start_goal_combination)
    print(city_combination - start_goal_combination)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    if m == 0:
        print(3)
        return
    # 都市を通る道路のリスト
    cities = [set() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        cities[a-1].add(b-1)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if i in cities[j]:
                continue
            for k in range(n):
                if i == k:
                    continue
                if j == k:
                    continue
                if i in cities[k]:
                    continue
                if j in cities[k]:
                    continue
                ans += 1
    print(ans)
