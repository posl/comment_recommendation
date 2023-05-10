Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)
    #print("")

    city = [0] * N
    for i in range(M):
        city[A[i]-1] += 1
        city[B[i]-1] += 1
    #print(city)
    #print("")

    for i in range(N):
        print(city[i])

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(n):
        c = 0
        d = []
        for j in range(m):
            if i+1 == a[j]:
                c += 1
                d.append(b[j])
            elif i+1 == b[j]:
                c += 1
                d.append(a[j])
        d.sort()
        print(c,end=" ")
        for j in range(len(d)):
            print(d[j],end=" ")
        print()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M, A, B)

    # 都市と道路の接続情報を管理する配列
    # 1-indexedで管理するため、N+1個の配列を用意
    # 都市iと道路で直接結ばれている都市はd[i]個ある
    d = [0] * (N+1)
    # 都市iと道路で直接結ばれている都市を昇順に管理する
    a = [[] for _ in range(N+1)]
    #print(d, a)

    # 都市iと道路で直接結ばれている都市を配列に格納
    for i in range(M):
        d[A[i]] += 1
        d[B[i]] += 1
        a[A[i]].append(B[i])
        a[B[i]].append(A[i])
    #print(d, a)

    # 出力
    for i in range(1, N+1):
        print(d[i], end = " ")
        for j in range(d[i]):
            print(a[i][j], end = " ")
        print()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        print(A.count(i+1) + B.count(i+1))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(1, N+1):
        l = []
        for j in range(M):
            if i == A[j]:
                l.append(B[j])
            elif i == B[j]:
                l.append(A[j])
        l.sort()
        print(len(l), *l)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(M):
        ans[A[i]][0] += 1
        ans[B[i]][0] += 1
        ans[A[i]][ans[A[i]][0]] = B[i]
        ans[B[i]][ans[B[i]][0]] = A[i]
    for i in range(1, N + 1):
        print(ans[i][0], end = "")
        for j in range(1, ans[i][0] + 1):
            print(" " + str(ans[i][j]), end = "")
        print("")

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x:(x[0], x[1]))

    cnt = 0
    for i in range(1, n+1):
        for j in range(m):
            if ab[j][0] == i:
                cnt += 1
            else:
                break
        print(cnt, end=' ')
        for j in range(m):
            if ab[j][0] == i:
                print(ab[j][1], end=' ')
            else:
                break
        print()
        ab = ab[cnt:]
        cnt = 0

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = [0] * n
    b = [0] * n
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(n):
        print(a.count(i+1) + b.count(i+1))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    for i in range(1, m + 1):
        a[i], b[i] = map(int, input().split())
    c = [0] * (n + 1)
    for i in range(1, m + 1):
        c[a[i]] += 1
        c[b[i]] += 1
    for i in range(1, n + 1):
        print(c[i])
