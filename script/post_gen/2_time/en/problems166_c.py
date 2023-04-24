Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(N, M)
    #print(H)
    #print(A)
    #print(B)

    good = [True] * N
    for i in range(M):
        if H[A[i]-1] <= H[B[i]-1]:
            good[A[i]-1] = False
        if H[B[i]-1] <= H[A[i]-1]:
            good[B[i]-1] = False

    print(sum(good))

main()

I think this is a good way to solve this problem.

I tried to solve this problem with the following code.

But it is too slow.

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    ans = 0
    for i in range(n):
        ok = True
        for j in g[i]:
            if h[i] <= h[j]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)
main()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = [a-1 for a in A]
    B = [b-1 for b in B]
    C = [0]*N
    for i in range(M):
        if H[A[i]] == H[B[i]]:
            C[A[i]] += 1
            C[B[i]] += 1
        elif H[A[i]] > H[B[i]]:
            C[B[i]] += 1
        else:
            C[A[i]] += 1
    ans = 0
    for i in range(N):
        if C[i] == 0:
            ans += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [None] * M
    B = [None] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M, H, A, B)
    G = [[] for _ in range(N)]
    for a, b in zip(A, B):
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    #print(G)
    ans = 0
    for i in range(N):
        flag = True
        for j in G[i]:
            if H[i] <= H[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    ans = 0
    for i in range(n):
        good = True
        for j in adj[i]:
            if h[i] <= h[j]:
                good = False
                break
        if good:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        ans += 1
        for a, b in AB:
            if a == i + 1 and H[i] <= H[b - 1]:
                ans -= 1
                break
            elif b == i + 1 and H[i] <= H[a - 1]:
                ans -= 1
                break
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    good = [True] * N
    for a, b in AB:
        if H[a-1] <= H[b-1]:
            good[a-1] = False
        if H[a-1] >= H[b-1]:
            good[b-1] = False
    print(sum(good))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    result = 0
    for i in range(N):
        for j in range(M):
            if AB[j][0] == i+1 and H[i] <= H[AB[j][1]-1]:
                break
            if AB[j][1] == i+1 and H[i] <= H[AB[j][0]-1]:
                break
        else:
            result += 1
    print(result)

=======
Suggestion 9

def  main():
     n ,  m  =  map ( int ,  input (). split ())
     h  =  list ( map ( int ,  input (). split ()))
     g  =  [ []  for  _  in  range ( n )]
     for  _  in  range ( m ):
         a ,  b  =  map ( int ,  input (). split ())
         g[ a  -  1 ]. append ( b  -  1 )
         g[ b  -  1 ]. append ( a  -  1 )
     ans  =  0 
     for  i  in  range ( n ):
         flag  =  True 
         for  j  in  g[ i ]:
             if  h[ i ] <= h[ j ]:
                 flag  =  False 
                 break 
         if  flag:
             ans  +=  1 
     print ( ans )

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    h = [int(i) for i in input().split()]
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    good = 0
    for i in range(n):
        flag = 0
        for j in range(m):
            if a[j] == i+1:
                if h[i] <= h[b[j]-1]:
                    flag = 1
                    break
            elif b[j] == i+1:
                if h[i] <= h[a[j]-1]:
                    flag = 1
                    break
        if flag == 0:
            good += 1
    print(good)
