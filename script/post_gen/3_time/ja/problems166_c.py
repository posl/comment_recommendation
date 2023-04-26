Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        flag = True
        for j in range(m):
            if a[j] == i + 1 and h[i] <= h[b[j] - 1]:
                flag = False
                break
            if b[j] == i + 1 and h[i] <= h[a[j] - 1]:
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
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        flag = 1
        for j in range(M):
            if AB[j][0] == i + 1:
                if H[i] <= H[AB[j][1] - 1]:
                    flag = 0
                    break
            if AB[j][1] == i + 1:
                if H[i] <= H[AB[j][0] - 1]:
                    flag = 0
                    break
        if flag == 1:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0 for i in range(M)]
    B = [0 for i in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    good = [True for i in range(N)]
    for i in range(M):
        if H[A[i]] >= H[B[i]]:
            good[B[i]] = False
        if H[B[i]] >= H[A[i]]:
            good[A[i]] = False
    ans = 0
    for i in range(N):
        if good[i]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(N, M)
    #print(H)
    #print(AB)
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if AB[j][0] == i + 1:
                if H[i] <= H[AB[j][1] - 1]:
                    flag = False
                    break
            elif AB[j][1] == i + 1:
                if H[i] <= H[AB[j][0] - 1]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    H.insert(0, 0)
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    ans = 0
    for i in range(1, N+1):
        flag = True
        for j in G[i]:
            if H[i] <= H[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(M):
            if AB[j][0]-1 == i:
                if H[i] <= H[AB[j][1]-1]:
                    break
            elif AB[j][1]-1 == i:
                if H[i] <= H[AB[j][0]-1]:
                    break
        else:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    #各展望台の隣接リスト
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    ans = 0
    for i in range(N):
        is_good = True
        for j in G[i]:
            if H[i] <= H[j]:
                is_good = False
                break
        if is_good:
            ans += 1

    print(ans)

=======
Suggestion 8

def main():
    # 1行目
    N, M = map(int, input().split())
    # 2行目
    H = list(map(int, input().split()))
    # 3行目以降
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 1. 道を繋ぐ2点の標高を比較
    # 2. 標高が同じなら、道を消す
    # 3. 標高が異なるなら、高い方の標高を保存
    # 4. 高い方の標高を保存した展望台は、良い展望台とする

    # 道を繋ぐ2点の標高を比較
    for i in range(M):
        # 標高が同じなら、道を消す
        if H[AB[i][0]-1] == H[AB[i][1]-1]:
            H[AB[i][0]-1] = 0
            H[AB[i][1]-1] = 0
        # 標高が異なるなら、高い方の標高を保存
        else:
            # 高い方の標高を保存した展望台は、良い展望台とする
            if H[AB[i][0]-1] < H[AB[i][1]-1]:
                H[AB[i][0]-1] = 0
            else:
                H[AB[i][1]-1] = 0

    # 良い展望台の数を出力
    print(sum(1 for i in H if i != 0))

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    h = list(map(int, input().split()))
    a = []
    b = []
    for i in range(m):
        a_,b_ = map(int, input().split())
        a.append(a_-1)
        b.append(b_-1)
    good = [1]*n
    for i in range(m):
        if h[a[i]] == h[b[i]]:
            good[a[i]] = 0
            good[b[i]] = 0
        elif h[a[i]] > h[b[i]]:
            good[b[i]] = 0
        else:
            good[a[i]] = 0
    print(sum(good))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    # まずは、各展望台の標高を高い順に並び替える
    H_ = sorted(H, reverse=True)
    # 標高の高い順に、展望台の番号を並べ替える
    H_ = [H.index(h) for h in H_]

    # 1. 各展望台について、展望台 i から一本の道を使って辿り着ける展望台は展望台 j と展望台 k である。
    # 2. 展望台 i の標高は展望台 j の標高より高く、かつ展望台 k の標高より高い。
    # という情報を、各展望台の標高を高い順に並び替えた上で、
    # 高い順に展望台の番号を並べ替えたものに対して、
    # 1. については、展望台 i から一本の道を使って辿り着ける展望台は展望台 j と展望台 k である。
    # という情報を記録しておく。
    # このとき、展望台 j と展望台 k のうち、標高が高い方を記録しておく。
    # 2. については、展望台 i の標高は展望台 j の標高より高く、かつ展望台 k の標高より高い。
    # という情報は、展望台 i の標高を高い順に
