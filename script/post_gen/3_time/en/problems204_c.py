Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = N*(N-1)
    for i in range(M):
        for j in range(M):
            if A[i] == A[j] and B[i] == B[j]:
                ans -= 1
    print(ans)

main()

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

    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            used = [False] * (N + 1)
            used[i] = True
            used[j] = True
            for k in range(M):
                if A[k] == i:
                    used[B[k]] = True
                if B[k] == i:
                    used[A[k]] = True
            if all(used):
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    ans = N*(N-1)
    for i in range(M):
        for j in range(i+1,M):
            if A[i] == A[j] and B[i] == B[j]:
                ans -= 1
            elif A[i] == B[j] and B[i] == A[j]:
                ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    road = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        road[A-1][B-1] = 1

    ans = 0
    for i in range(N):
        for j in range(N):
            if road[i][j] == 0:
                continue
            for k in range(N):
                if road[j][k] == 1:
                    road[i][k] = 1

    for i in range(N):
        for j in range(N):
            if road[i][j] == 1:
                ans += 1

    print(ans)

=======
Suggestion 5

def main():
    #input
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #count
    ans = 0
    for i in range(M):
        ans += N-1
        for j in range(M):
            if A[i] == B[j]:
                ans -= 1
            if B[i] == A[j]:
                ans -= 1
    #output
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
    #print(AB)
    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[2][0])
    #print(AB[2][1])
    #print(AB[3][0])
    #print(AB[3][1])
    #print(AB[4][0])
    #print(AB[4][1])
    #print(AB[5][0])
    #print(AB[5][1])
    #print(AB[6][0])
    #print(AB[6][1])
    #print(AB[7][0])
    #print(AB[7][1])
    #print(AB[8][0])
    #print(AB[8][1])
    #print(AB[9][0])
    #print(AB[9][1])
    #print(AB[10][0])
    #print(AB[10][1])
    #print(AB[11][0])
    #print(AB[11][1])
    #print(AB[12][0])
    #print(AB[12][1])
    #print(AB[13][0])
    #print(AB[13][1])
    #print(AB[14][0])
    #print(AB[14][1])
    #print(AB[15][0])
    #print(AB[15][1])
    #print(AB[16][0])
    #print(AB[16][1])
    #print(AB[17][0])
    #print(AB[17][1])
    #print(AB[18][0])
    #print(AB[18][1])
    #print(AB[19][0])
    #print(AB[19][1])
    #print(AB[20][0])
    #print(AB[20][1])
    #print(AB[21][0])
    #print(AB[21][1])
    #

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    #A = [0] * M
    #B = [0] * M
    AB = [[0,0]] * M
    for i in range(M):
        AB[i] = list(map(int, input().split()))
        #A[i], B[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)
    #print(AB)
    
    #print(AB[0][0],AB[0][1])
    #print(AB[1][0],AB[1][1])
    #print(AB[2][0],AB[2][1])
    #print(AB[3][0],AB[3][1])

    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[2][0])
    #print(AB[2][1])
    #print(AB[3][0])
    #print(AB[3][1])
    
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[3][0])
    #print(AB[3][1])
    
    #print(AB[1][0] == AB[3][0])
    #print(AB[1][0] == AB[3][1])
    
    #print(AB[1][1] == AB[3][0])
    #print(AB[1][1] == AB[3][1])
    
    #print(AB[1][0] == AB[3][1] and AB[1][1] == AB[3][0])
    
    #print(AB[1][0] == AB[3][1] and AB[1][1] == AB[3][0])
    
    #print(AB[1][0] == AB[3][0] or AB[1][0] == AB[3][1])
    #print(AB[1][1] == AB[3][0] or AB[1][1] == AB[3][1])
    
    #print(AB[1][0] == AB

=======
Suggestion 8

def main():
    # N: number of cities
    # M: number of roads
    N, M = map(int, input().split())
    # A: city A_i
    # B: city B_i
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # count: number of pairs of cities that can be the origin and destination
    count = 0
    for i in range(N):
        count += N-1
        for j in range(M):
            if A[j] == i+1 or B[j] == i+1:
                count -= 1
    print(count)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # A_i, B_iの入力を受け取る
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 頂点1からの到達可能な頂点を集める
    # 頂点1からの到達可能な頂点の集合を求める
    # 頂点1からの到達可能な頂点の集合
    reachable = set()
    # 頂点1からの到達可能な頂点を集める
    for i in range(M):
        if A[i] == 1:
            reachable.add(B[i])
    # 頂点1からの到達可能な頂点の集合から、さらに到達可能な頂点を集める
    # 頂点1からの到達可能な頂点の集合のサイズ
    size = len(reachable)
    # reachableの要素の数が変わらなくなるまで繰り返す
    while True:
        # reachableの要素の数
        size = len(reachable)
        # 頂点1からの到達可能な頂点の集合から、さらに到達可能な頂点を集める
        for i in range(M):
            if A[i] in reachable:
                reachable.add(B[i])
        # reachableの要素の数が変わらなくなったら、while文を抜ける
        if size == len(reachable):
            break
    # 頂点1からの到達可能な頂点の集合の要素の数
    print(len(reachable))
    return 0

=======
Suggestion 10

def main():
    #Read input
    N, M = map(int, input().split())
    #Roads
    roads = []
    for i in range(M):
        a, b = map(int, input().split())
        roads.append([a, b])
    #Count
    cnt = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            #Check if a road exists
            road_exists = False
            for k in range(M):
                if roads[k][0] == i and roads[k][1] == j:
                    road_exists = True
            if road_exists:
                cnt += 1
    #Output
    print(cnt)
