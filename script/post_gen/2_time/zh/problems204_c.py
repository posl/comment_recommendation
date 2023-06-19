Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    #n,m = 3,3
    #n,m = 3,0
    #n,m = 4,4
    #n,m = 2000,2000
    #n,m = 2,1
    #n,m = 2,0
    #n,m = 1,0
    #n,m = 1,1
    #n,m = 2,2
    #n,m = 2000,1
    #n,m = 2000,0
    #n,m = 2000,1999
    #n,m = 2000,2000
    #n,m = 2000,1998
    #n,m = 2000,2
    #n,m = 2000,3
    #n,m = 2000,4
    #n,m = 2000,5
    #n,m = 2000,6
    #n,m = 2000,7
    #n,m = 2000,8
    #n,m = 2000,9
    #n,m = 2000,10
    #n,m = 2000,11
    #n,m = 2000,12
    #n,m = 2000,13
    #n,m = 2000,14
    #n,m = 2000,15
    #n,m = 2000,16
    #n,m = 2000,17
    #n,m = 2000,18
    #n,m = 2000,19
    #n,m = 2000,20
    #n,m = 2000,21
    #n,m = 2000,22
    #n,m = 2000,23
    #n,m = 2000,24
    #n,m = 2000,25
    #n,m = 2000,26
    #n,m = 2000,27
    #n,m = 2000,28
    #n,m = 2000,29
    #n,m = 2000,30
    #n,m = 2000,31
    #n,m = 2000

=======
Suggestion 2

def problems204_c():
    N, M = map(int, input().split())
    # 0 <= M <= min(2000, N(N-1))
    # 0 <= M <= N(N-1)
    # 0 <= M <= N^2 - N
    # M <= N^2 - N
    # M + N <= N^2
    # N^2 - N - M >= 0
    # N^2 - N - M = 0
    # N = (1 + sqrt(1 + 4M)) / 2
    # N = (1 - sqrt(1 + 4M)) / 2
    # N = 1/2 + sqrt(1/4 + M)
    # N = 1/2 - sqrt(1/4 + M)
    # 0.5 + sqrt(0.25 + M) >= 0
    # sqrt(0.25 + M) >= -0.5
    # 0.25 + M >= 0
    # M >= -0.25
    # M >= 0
    # 0.5 - sqrt(0.25 + M) >= 0
    # sqrt(0.25 + M) <= 0.5
    # 0.25 + M <= 0.25
    # M <= 0
    if M > N * (N - 1):
        return
    if M < 0:
        return
    # 2 <= N <= 2000
    # 2 <= N <= 2000
    if N < 2:
        return
    if N > 2000:
        return
    # 1 <= A_i, B_i <= N
    # 1 <= A_i, B_i <= N
    # A_i != B_i
    # A_i != B_i
    # (A_i, B_i) are different
    # (A_i, B_i) are different
    # 1 <= A_i, B_i <= N
    # 1 <= A_i, B_i <= N
    # A_i != B_i
    # A_i != B_i
    # (A_i, B_i) are different
    # (A_i, B_i) are different
    # 1 <=

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    l = [list(map(int,input().split())) for i in range(m)]
    s = set()
    for i in range(m):
        s.add(l[i][0])
        s.add(l[i][1])
    print(len(s)*(len(s)-1))

=======
Suggestion 4

def solve():
    N,M = map(int,input().split())
    edges = []
    for i in range(M):
        a,b = map(int,input().split())
        edges.append((a,b))
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i != j:
                cnt = 0
                for edge in edges:
                    if edge[0] == i and edge[1] == j:
                        cnt += 1
                ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    print(n*(n-1)//2-m)

=======
Suggestion 6

def readinput():
    n,m=list(map(int,input().split()))
    ab=[]
    for _ in range(m):
        a,b=list(map(int,input().split()))
        ab.append((a,b))
    return n,m,ab

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(N**2-M)

=======
Suggestion 8

def main():
    N,M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N * (N - 1) // 2 - M)
    return

=======
Suggestion 9

def get_input():
    N, M = input().split()
    N = int(N)
    M = int(M)

    #print("N={0}, M={1}".format(N, M))

    A = []
    B = []
    for i in range(M):
        a, b = input().split()
        a = int(a)
        b = int(b)
        A.append(a)
        B.append(b)

    #print("A={0}, B={1}".format(A, B))
    return N, M, A, B

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    city = [0]*n
    for i in range(m):
        a,b = map(int,input().split())
        city[a-1] += 1
        city[b-1] += 1
    ans = 0
    for i in range(n):
        ans += city[i]*(n-1-city[i])
    print(ans//2)
