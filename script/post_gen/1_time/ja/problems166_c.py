Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j] == i + 1:
                if H[A[j] - 1] <= H[B[j] - 1]:
                    flag = False
                    break
            elif B[j] == i + 1:
                if H[B[j] - 1] <= H[A[j] - 1]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    ans = 0
    for i in range(N):
        ok = True
        for j in G[i]:
            if H[i] <= H[j]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j] == i:
                if H[i] <= H[B[j]]:
                    flag = False
                    break
            elif B[j] == i:
                if H[i] <= H[A[j]]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    cnt = 0
    for i in range(n):
        ok = True
        for j in g[i]:
            if h[i] <= h[j]:
                ok = False
                break
        if ok:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(M):
            if AB[j][0] == i+1 and H[AB[j][0]-1] <= H[AB[j][1]-1]:
                flag = 1
            elif AB[j][1] == i+1 and H[AB[j][1]-1] <= H[AB[j][0]-1]:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    #入力
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    #初期化
    good = [1] * N

    #処理
    for a, b in AB:
        if H[a - 1] > H[b - 1]:
            good[b - 1] = 0
        elif H[a - 1] < H[b - 1]:
            good[a - 1] = 0
        else:
            good[a - 1] = 0
            good[b - 1] = 0

    #出力
    print(sum(good))

=======
Suggestion 7

def main():
    #入力
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0 for i in range(M)]
    B = [0 for i in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    #処理
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j] == i+1 and H[i] <= H[B[j]-1]:
                flag = False
                break
            elif B[j] == i+1 and H[i] <= H[A[j]-1]:
                flag = False
                break
        if flag:
            ans += 1
    #出力
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(H)
    #print(AB)
    #print(N, M)
    #print(H)
    #print(AB)
    #print(N, M)
    #print(H)
    #print(AB)
    count = 0
    for i in range(0, N):
        #print("i:", i)
        for j in range(0, M):
            #print("j:", j)
            if AB[j][0] == i + 1:
                #print("AB[j][0] == i + 1", AB[j][0], i + 1)
                #print(H[i], H[AB[j][1] - 1])
                if H[i] <= H[AB[j][1] - 1]:
                    #print("H[i] <= H[AB[j][1] - 1]", H[i], H[AB[j][1] - 1])
                    break
            elif AB[j][1] == i + 1:
                #print("AB[j][1] == i + 1", AB[j][1], i + 1)
                #print(H[i], H[AB[j][0] - 1])
                if H[i] <= H[AB[j][0] - 1]:
                    #print("H[i] <= H[AB[j][0] - 1]", H[i], H[AB[j][0] - 1])
                    break
            if j == M - 1:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    
    # 各展望台の良い展望台の数をカウントするリスト
    count = [0] * N
    
    for i in range(M):
        # 道を結ぶ展望台の標高を比較
        if H[AB[i][0] - 1] > H[AB[i][1] - 1]:
            # 展望台1の方が標高が高い場合
            count[AB[i][1] - 1] += 1
        elif H[AB[i][0] - 1] < H[AB[i][1] - 1]:
            # 展望台2の方が標高が高い場合
            count[AB[i][0] - 1] += 1
    
    # 良い展望台の数
    ans = count.count(0)
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 1. 道のある展望台の中で最も標高が高い展望台を探す
    # 2. 道のある展望台の中で最も標高が高い展望台と同じ標高の展望台があれば、それも良い展望台になる
    # 3. 1. 2. が当てはまらない展望台は良い展望台となる

    # 1. と 2. を行う
    # 道のある展望台の中で最も標高が高い展望台を探す
    # 道のある展望台の中で最も標高が高い展望台と同じ標高の展望台があれば、それも良い展望台になる
    # 2. を行うために、展望台の標高とその展望台と道でつながっている展望台の標高を
    # それぞれリストに格納しておく
    # また、展望台の標高とその展望台の標高が同じかどうかを判定するリストも作成する
    # 道のある展望台の中で最も標高が高い展望台を探す
    # 道のある展望台の中で最も標高が高い展望台と同じ標高の展望台があれば、それも良い展望台になる
    # 2. を行うために、展望台の標
