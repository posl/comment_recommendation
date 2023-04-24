Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    for i in range(N):
        print(A.index(A[i]) + 1, B.index(B[i]) + 1)

=======
Suggestion 2

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    for i in range(N):
        print(A.index(A[i])+1, B.index(B[i])+1)

=======
Suggestion 3

def main():
    h, w, n = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    for i in range(n):
        print(a.index(a[i])+1, b.index(b[i])+1)

=======
Suggestion 4

def main():
    H,W,N = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    A.sort()
    B.sort()
    C = [0]*N
    D = [0]*N
    for i in range(N):
        C[i] = A.index(A[i])+1
        D[i] = B.index(B[i])+1
    for i in range(N):
        print(C[i],D[i])

=======
Suggestion 5

def main():
    H,W,N = map(int,input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    A.sort()
    B.sort()
    for i in range(N):
        print(A[i] - bisect.bisect_left(A,A[i]) + 1,B[i] - bisect.bisect_left(B,B[i]) + 1)

=======
Suggestion 6

def main():
    h,w,n = map(int,input().split())
    #print(h,w,n)
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i],b[i] = map(int,input().split())
        #print(a[i],b[i])
    #print(a)
    #print(b)
    a = list(set(a))
    a.sort()
    b = list(set(b))
    b.sort()
    #print(a)
    #print(b)
    for i in range(n):
        print(a.index(a[i])+1,b.index(b[i])+1)

=======
Suggestion 7

def main():
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # 重複を排除した座標を得る
    A = sorted(set([ab[0] for ab in AB]))
    B = sorted(set([ab[1] for ab in AB]))

    # 座標の変換
    for i in range(N):
        # 重複を排除した座標の順番を得る
        a = bisect.bisect_left(A, AB[i][0])
        b = bisect.bisect_left(B, AB[i][1])
        print(a+1, b+1)
