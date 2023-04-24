Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = [0] * N
    X = [[0] * N for _ in range(N)]
    Y = [[0] * N for _ in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][j] = x
            Y[i][j] = y

    ans = 0
    for bit in range(1 << N):
        flag = True
        for i in range(N):
            if (bit >> i) & 1:
                for j in range(A[i]):
                    x = X[i][j] - 1
                    y = Y[i][j]
                    if y == 1:
                        if (bit >> x) & 1:
                            continue
                        else:
                            flag = False
                            break
                    elif y == 0:
                        if (bit >> x) & 1:
                            flag = False
                            break
                        else:
                            continue
                if flag == False:
                    break
        if flag:
            ans = max(ans, bin(bit).count("1"))

    print(ans)

=======
Suggestion 2

def   main (): 
     N   =   int ( input ()) 
     A   =   [] 
     for   i   in   range ( N ): 
         A . append ( int ( input ())) 
         for   j   in   range ( A [ i ]): 
             x ,   y   =   map ( int ,   input (). split ()) 

     print ( N )

=======
Suggestion 3

def main():
    N = int(input())
    A = [0]*N
    x = [[] for i in range(N)]
    y = [[] for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x[i].append(0)
            y[i].append(0)
            x[i][j],y[i][j] = map(int,input().split())
    ans = 0
    for i in range(2**N):
        flg = True
        for j in range(N):
            if flg == False:
                break
            if ((i>>j)&1):
                for k in range(A[j]):
                    if y[j][k] == 1:
                        if ((i>>(x[j][k]-1))&1) == 0:
                            flg = False
                            break
                    else:
                        if ((i>>(x[j][k]-1))&1) == 1:
                            flg = False
                            break
        if flg:
            ans = max(ans,bin(i).count("1"))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = [0]*N
    X = [[] for i in range(N)]
    Y = [[] for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x)
            Y[i].append(y)
    ans = 0
    for i in range(2**N):
        honest = [0]*N
        for j in range(N):
            if (i >> j) & 1:
                honest[j] = 1
        flag = True
        for j in range(N):
            if honest[j]:
                for k in range(A[j]):
                    if honest[X[j][k]-1] != Y[j][k]:
                        flag = False
        if flag:
            ans = max(ans, honest.count(1))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([int(x) for x in input().split()])
        for j in range(A[i][0]):
            A[i].append([int(x) for x in input().split()])
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(N):
            if i >> j & 1:
                for k in range(A[j][0]):
                    if A[j][k+1][1] == 1 and not i >> A[j][k+1][0]-1 & 1:
                        flag = False
                        break
                    if A[j][k+1][1] == 0 and i >> A[j][k+1][0]-1 & 1:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 6

def   main (): 
     N   =   int ( input ()) 
     A   =   [] 
     for   i   in   range ( N ): 
         A_i   =   int ( input ()) 
         A_i_list   =   [] 
         for   j   in   range ( A_i ): 
             x ,   y   =   map ( int ,   input (). split ()) 
             A_i_list . append (( x ,   y )) 
         A . append ( A_i_list ) 

     ans   =   0 
     for   i   in   range ( 2 ** N ): 
         honest   =   [ False   for   j   in   range ( N )] 
         for   j   in   range ( N ): 
             if   (( i   >>   j )   &   1 ): 
                 honest [ j ]   =   True 
         flag   =   True 
         for   j   in   range ( N ): 
             if   honest [ j ]: 
                 for   x ,   y   in   A [ j ]: 
                     if   y   ==   1 : 
                         if   not   honest [ x   -   1 ]: 
                             flag   =   False 
                     else : 
                         if   honest [ x   -   1 ]: 
                             flag   =   False 
         if   flag : 
             ans   =   max ( ans ,   honest . count ( True )) 

     print ( ans )

=======
Suggestion 7

def   main ():
     N   =   int ( input ())
     A   =   [ 0   for   _   in   range ( N )]
     X   =   [ []   for   _   in   range ( N )]
     Y   =   [ []   for   _   in   range ( N )]
     for   i   in   range ( N ):
         A [ i ]   =   int ( input ())
         for   j   in   range ( A [ i ]):
             x ,   y   =   map ( int ,   input (). split ())
             X [ i ]. append ( x - 1 )
             Y [ i ]. append ( y )

     ans   =   0 
     for   bit   in   range ( 2 ** N ):
         ok   =   True 
         for   i   in   range ( N ):
             if   ( bit   >>   i )   &   1 :
                 for   j   in   range ( A [ i ]):
                     if   Y [ i ][ j ]   ==   1 :
                         if   not   ( bit   >>   X [ i ][ j ])   &   1 :
                             ok   =   False 
                     else :
                         if   ( bit   >>   X [ i ][ j ])   &   1 :
                             ok   =   False 
         if   ok :
             ans   =   max ( ans ,   bin ( bit ). count ( "1" ))
     print ( ans )

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])

    ans = 0
    for i in range(2 ** n):
        bit = [0] * n
        for j in range(n):
            if (i >> j) & 1:
                bit[j] = 1
        flag = True
        for j in range(n):
            if bit[j] == 1:
                for k in range(1, a[j][0] + 1):
                    x = a[j][2 * k - 1] - 1
                    y = a[j][2 * k]
                    if bit[x] != y:
                        flag = False
        if flag:
            ans = max(ans, sum(bit))

    print(ans)

=======
Suggestion 9

def   main ():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    x = [[0] * N for _ in range(N)]
    y = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
            x[i][j] -= 1

    ans = 0
    for i in range(2 ** N):
        ok = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if y[j][k] == 1:
                        if not ((i >> x[j][k]) & 1):
                            ok = False
                    else:
                        if (i >> x[j][k]) & 1:
                            ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))

    print(ans)

=======
Suggestion 10

def dfs(N, A, x, y, honest, i):
    if i == N:
        for j in range(N):
            for k in range(A[j]):
                if honest[j] != honest[x[j][k] - 1] == y[j][k]:
                    return 0
        return honest.count(1)

    honest[i] = 1
    res = dfs(N, A, x, y, honest, i + 1)
    honest[i] = 0
    res = max(res, dfs(N, A, x, y, honest, i + 1))
    return res
