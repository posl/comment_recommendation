Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    #print(C)
    #print(A)

    import itertools
    # 2**N通りの組み合わせを全探索
    # それぞれの組み合わせについて、アルゴリズムの理解度を計算する
    # その中から、理解度がX以上のものを探す
    # その中で、最もコストが小さいものを求める

    # 2**N通りの組み合わせを全探索
    min_cost = 10**9
    for i in range(2**N):
        #print(i)
        # 2進数に変換
        bin_i = bin(i)[2:]
        #print(bin_i)
        # 左詰めにする
        bin_i = bin_i.zfill(N)
        #print(bin_i)
        #print(bin_i[0])
        #print(bin_i[1])

        # それぞれの組み合わせについて、アルゴリズムの理解度を計算する
        # それぞれの理解度を0で初期化
        a = [0] * M
        #print(a)
        cost = 0
        for j in range(N):
            #print(j)
            #print(bin_i[j])
            if bin_i[j] == "1":
                #print("1")
                #print(j)
                #print(C[j])
                cost += C[j]
                #print(a)
                #print(A[j])
                for k in range(M):
                    #print(k)
                    #print(A[j][k])
                    a[k] += A[j][k]
                    #print(a)
        #print(a)

        # その中から、理解度がX以上のものを探す
        is_ok = True
        for j in range(M):
            if a[j] < X:

=======
Suggestion 2

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10 ** 9
    for i in range(2 ** N):
        cost = 0
        a = [0] * M
        for j in range(N):
            if i & (1 << j):
                cost += C[j]
                for k in range(M):
                    a[k] += A[j][k]
        if all(x >= X for x in a):
            min_cost = min(min_cost, cost)
    print(min_cost if min_cost < 10 ** 9 else -1)

=======
Suggestion 3

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        C.append(tmp[0])
        A.append(tmp[1:])
    ans = 10**9 + 1
    for i in range(2**N):
        cost = 0
        tmp = [0 for i in range(M)]
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    tmp[k] += A[j][k]
        for j in range(M):
            if tmp[j] < X:
                break
        else:
            ans = min(ans, cost)
    print(-1 if ans == 10**9 + 1 else ans)

=======
Suggestion 4

def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [[0] * M for _ in range(N)]
    for i in range(N):
        C[i], *A[i] = map(int, input().split())

    ans = 10**10
    for bit in range(1 << N):
        cost = 0
        level = [0] * M
        for i in range(N):
            if bit & (1 << i):
                cost += C[i]
                for j in range(M):
                    level[j] += A[i][j]
        if min(level) >= X:
            ans = min(ans, cost)

    if ans == 10**10:
        print(-1)
    else:
        print(ans)

=======
Suggestion 5

def readinput():
    n,m,x=map(int,input().split())
    c=[]
    a=[]
    for _ in range(n):
        line=list(map(int,input().split()))
        c.append(line[0])
        a.append(line[1:])
    return n,m,x,c,a

=======
Suggestion 6

def main():
    n, m, x = map(int, input().split())
    c = [0] * n
    a = [[0] * m for i in range(n)]
    for i in range(n):
        c[i], *a[i] = map(int, input().split())

    ans = 10**9 + 1
    for i in range(2**n):
        cost = 0
        level = [0] * m
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans, cost)
    if ans == 10**9 + 1:
        ans = -1
    print(ans)

=======
Suggestion 7

def main():
    n, m, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = float('inf')
    for i in range(2**n):
        b = [0] * m
        cost = 0
        for j in range(n):
            if i >> j & 1:
                cost += a[j][0]
                for k in range(m):
                    b[k] += a[j][k+1]
        if min(b) >= x:
            ans = min(ans, cost)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 8

def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**10
    for i in range(2**N):
        t = [0]*(M+1)
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M+1):
                    t[k] += A[j][k]
        if all(t[k] >= X for k in range(1, M+1)):
            ans = min(ans, t[0])
    if ans == 10**10:
        print(-1)
    else:
        print(ans)

=======
Suggestion 9

def main():
    N, M, X = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    ans = -1
    for i in range(2**N):
        cost = 0
        level = [0]*M
        for j in range(N):
            if (i>>j) & 1:
                cost += A[j][0]
                for k in range(M):
                    level[k] += A[j][k+1]
        if min(level) >= X:
            if ans == -1:
                ans = cost
            else:
                ans = min(ans, cost)
    print(ans)

=======
Suggestion 10

def main():
    N, M, X = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    ans = 10**9
    for i in range(2**N):
        tmp = [0] * M
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                cost += A[j][0]
                for k in range(M):
                    tmp[k] += A[j][k + 1]
        if all(x >= X for x in tmp):
            ans = min(ans, cost)
    print(ans if ans != 10**9 else -1)
    return
