Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    
    # 1からNの都市の組み合わせの数をカウントする
    count = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            
            # 道路がない場合はカウントしない
            for k in range(M):
                if (A[k] == i and B[k] == j) or (A[k] == j and B[k] == i):
                    count += 1
                    break
    
    print(count)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N * (N - 1) - M)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(N*(N-1)-M)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0 for _ in range(M)]
    B = [0 for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N * (N - 1) - M)

=======
Suggestion 5

def main():
    N, M = map(int,input().split())
    A = [0]*M
    B = [0]*M

    for i in range(M):
        A[i], B[i] = map(int,input().split())

    ans = 0
    for i in range(M):
        for j in range(i+1,M):
            if A[i] == A[j] or A[i] == B[j] or B[i] == A[j] or B[i] == B[j]:
                ans += 1

    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N * N)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            if AB[i][1] < AB[j][0]:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(m)]
    print(n * (n - 1) - m)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    #都市の組み合わせをリスト化
    city = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            city.append([i, j])
    #道路の組み合わせをリスト化
    road = []
    for i in range(M):
        road.append(list(map(int, input().split())))
    #都市の組み合わせから道路の組み合わせを除外
    for i in range(len(city)):
        for j in range(len(road)):
            if city[i] == road[j]:
                city[i] = [0, 0]
    #都市の組み合わせからスタート地点とゴール地点が同じものを除外
    for i in range(len(city)):
        if city[i][0] == city[i][1]:
            city[i] = [0, 0]
    #都市の組み合わせからスタート地点とゴール地点が同じものを除外
    for i in range(len(city)):
        if city[i][0] == city[i][1]:
            city[i] = [0, 0]
    #都市の組み合わせから[0, 0]を除外
    city = [i for i in city if i != [0, 0]]
    #都市の組み合わせの数を出力
    print(len(city))

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict

    n,m = map(int, sys.stdin.readline().split())
    if m == 0:
        print(n**2)
        return

    dic = defaultdict(set)
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        dic[a].add(b)

    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if j in dic[i]:
                continue
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # 都市の数だけ0のリストを用意する
    city = [0] * N
    # 都市の数だけ、その都市に到達できる都市のリストを用意する
    city_list = [[] for i in range(N)]
    # 道路の数だけ、道路の両端の都市を取得する
    for i in range(M):
        A, B = map(int, input().split())
        # 都市のリストに、到達できる都市を追加する
        city_list[A-1].append(B-1)
    # 都市の数だけ繰り返す
    for i in range(N):
        # 都市のリストを繰り返す
        for j in city_list[i]:
            # 都市のリストの中身を繰り返す
            for k in city_list[j]:
                # 到達できる都市が、その都市自身でなければ、
                # その都市に到達できる都市のリストに追加する
                if k != i:
                    city_list[i].append(k)
    # 都市の数だけ繰り返す
    for i in range(N):
        # 都市のリストの重複を削除する
        city_list[i] = list(set(city_list[i]))
        # 都市のリストの数を、都市のリストの数だけ増やす
        city[i] = len(city_list[i])
    # 都市の数の2乗を出力する
    print(sum(city) ** 2)
