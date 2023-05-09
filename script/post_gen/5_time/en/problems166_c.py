Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    count = 0
    for i in range(N):
        is_good = True
        for j in range(M):
            if i+1 == A[j]:
                if H[i] <= H[B[j]-1]:
                    is_good = False
            elif i+1 == B[j]:
                if H[i] <= H[A[j]-1]:
                    is_good = False
        if is_good:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(N, M, H, A, B)

    #print(N, M, H, A, B)

    good = [True for i in range(N)]

    for i in range(M):
        if H[A[i]-1] <= H[B[i]-1]:
            good[A[i]-1] = False
        if H[A[i]-1] >= H[B[i]-1]:
            good[B[i]-1] = False

    #print(good)

    print(good.count(True))

main()

=======
Suggestion 3

def main():
    N, M = [int(x) for x in input().split()]
    H = [int(x) for x in input().split()]
    A = []
    B = []
    for i in range(M):
        a, b = [int(x) for x in input().split()]
        A.append(a)
        B.append(b)
    #print(N, M, H, A, B)
    #print(H[A[0]-1], H[B[0]-1])
    #print(H[A[1]-1], H[B[1]-1])
    #print(H[A[2]-1], H[B[2]-1])
    #print(H[A[3]-1], H[B[3]-1])
    #print(H[A[4]-1], H[B[4]-1])
    good = [True] * N
    for i in range(M):
        if H[A[i]-1] <= H[B[i]-1]:
            good[A[i]-1] = False
        if H[B[i]-1] <= H[A[i]-1]:
            good[B[i]-1] = False
    #print(good)
    print(good.count(True))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    if N == 1:
        print(1)
        return

    good = [True] * N
    for a, b in AB:
        if H[a - 1] <= H[b - 1]:
            good[a - 1] = False
        if H[b - 1] <= H[a - 1]:
            good[b - 1] = False

    print(good.count(True))

=======
Suggestion 5

def main():
    #N, M = map(int, input().split())
    #H = list(map(int, input().split()))
    #AB = [list(map(int, input().split())) for _ in range(M)]
    #N, M = 4, 3
    #H = [1, 2, 3, 4]
    #AB = [[1, 3], [2, 3], [2, 4]]
    #N, M = 6, 5
    #H = [8, 6, 9, 1, 2, 1]
    #AB = [[1, 3], [4, 2], [4, 3], [4, 6], [4, 6]]
    N, M = 6, 5
    H = [8, 6, 9, 1, 2, 1]
    AB = [[1, 3], [4, 2], [4, 3], [4, 6], [4, 6]]
    #N, M = 6, 5
    #H = [8, 6, 9, 1, 2, 1]
    #AB = [[1, 3], [4, 2], [4, 3], [4, 6], [4, 6]]
    #N, M = 6, 5
    #H = [8, 6, 9, 1, 2, 1]
    #AB = [[1, 3], [4, 2], [4, 3], [4, 6], [4, 6]]
    #N, M = 6, 5
    #H = [8, 6, 9, 1, 2, 1]
    #AB = [[1, 3], [4, 2], [4, 3], [4, 6], [4, 6]]
    #N, M = 6, 5
    #H = [8, 6, 9, 1, 2, 1]
    #AB = [[1, 3], [4, 2], [4, 3], [4, 6], [4, 6

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    AB = [list(map(int,input().split())) for _ in range(M)]
    good = [True for _ in range(N)]
    for i in range(M):
        if H[AB[i][0]-1] <= H[AB[i][1]-1]:
            good[AB[i][0]-1] = False
        if H[AB[i][0]-1] >= H[AB[i][1]-1]:
            good[AB[i][1]-1] = False
    print(good.count(True))

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    AB = [list(map(int,input().split())) for _ in range(M)]
    good = [True]*N
    for i in range(M):
        if H[AB[i][0]-1] >= H[AB[i][1]-1]:
            good[AB[i][1]-1] = False
        if H[AB[i][0]-1] <= H[AB[i][1]-1]:
            good[AB[i][0]-1] = False
    print(good.count(True))

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    AB = [list(map(int,input().split())) for _ in range(M)]
    #print(N,M,H,AB)
    #print(N,M,H)
    #print(AB)
    #print()
    ans = N
    for ab in AB:
        if H[ab[0]-1] <= H[ab[1]-1]:
            ans -= 1
        if H[ab[0]-1] >= H[ab[1]-1]:
            ans -= 1
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    ab = []
    for i in range(m):
        ab.append(list(map(int,input().split())))

    #print(n,m,h,ab)

    # 隣接リストを作成する
    # 1から始まるので、0番目はダミー
    adjacent_list = [[] for i in range(n+1)]
    for i in range(m):
        adjacent_list[ab[i][0]].append(ab[i][1])
        adjacent_list[ab[i][1]].append(ab[i][0])

    #print(adjacent_list)

    # 隣接リストを作成する
    # 1から始まるので、0番目はダミー
    adjacent_list = [[] for i in range(n+1)]
    for i in range(m):
        adjacent_list[ab[i][0]].append(ab[i][1])
        adjacent_list[ab[i][1]].append(ab[i][0])

    #print(adjacent_list)

    # 隣接する頂点の高さを比較する
    # 高ければ、goodでない
    # 低ければ、good
    # 1から始まるので、0番目はダミー
    good = 0
    for i in range(1,n+1):
        #print(i,adjacent_list[i])
        flag = True
        for j in adjacent_list[i]:
            if h[i-1] <= h[j-1]:
                flag = False
        if flag:
            good += 1

    print(good)

=======
Suggestion 10

def get_max(a,b):
    if a>b:
        return a
    else:
        return b
