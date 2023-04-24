Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] * N
    X = [[0] * N for _ in range(N)]
    Y = [[0] * N for _ in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            X[i][j], Y[i][j] = map(int, input().split())
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1 and ((i >> (X[j][k] - 1)) & 1) != 1:
                        flag = False
                    if Y[j][k] == 0 and ((i >> (X[j][k] - 1)) & 1) == 1:
                        flag = False
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0] * N for _ in range(N)]
    Y = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][j] = x
            Y[i][j] = y

    for i in range(2 ** N):
        bit = bin(i)[2:].zfill(N)
        flag = True
        for j in range(N):
            if bit[j] == '1':
                for k in range(A[j]):
                    if bit[X[j][k] - 1] == '1' and Y[j][k] == 0:
                        flag = False
                    elif bit[X[j][k] - 1] == '0' and Y[j][k] == 1:
                        flag = False

        if flag:
            print(bit.count('1'))

=======
Suggestion 3

def main():
    N = int(input())
    A = [0] * N
    X = [[0] * N for i in range(N)]
    Y = [[0] * N for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            X[i][j], Y[i][j] = map(int, input().split())

    ans = 0
    for bit in range(1 << N):
        flag = True
        for i in range(N):
            if bit & (1 << i):
                for j in range(A[i]):
                    if Y[i][j] == 1:
                        if bit & (1 << (X[i][j] - 1)) == 0:
                            flag = False
                    else:
                        if bit & (1 << (X[i][j] - 1)) != 0:
                            flag = False
        if flag:
            ans = max(ans, bin(bit).count("1"))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0 for _ in range(N)] for _ in range(N)]
    Y = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][x-1] = 1
            Y[i][x-1] = y
    ans = 0
    for i in range(2**N):
        bit = [0 for _ in range(N)]
        for j in range(N):
            if (i >> j) & 1:
                bit[j] = 1
        flag = True
        for j in range(N):
            if bit[j] == 1:
                for k in range(N):
                    if X[j][k] == 1 and bit[k] != Y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, sum(bit))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0 for _ in range(N)] for _ in range(N)]
    Y = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][x - 1] = 1
            Y[i][x - 1] = y
    ans = 0
    for i in range(1 << N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(N):
                    if X[j][k] == 1 and ((i >> k) & 1) != Y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = [0] * N
    x = [[0] * N for i in range(N)]
    y = [[0] * N for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(2 ** N):
        isOK = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if y[j][k] == 1:
                        if not ((i >> (x[j][k] - 1)) & 1):
                            isOK = False
                    else:
                        if (i >> (x[j][k] - 1)) & 1:
                            isOK = False
        if isOK:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [0] * N
    x = [[0] * N for i in range(N)]
    y = [[0] * N for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())

    ans = 0
    for i in range(2 ** N):
        honest = [0] * N
        for j in range(N):
            if ((i >> j) & 1):
                honest[j] = 1

        flag = True
        for j in range(N):
            if honest[j] == 1:
                for k in range(A[j]):
                    if honest[x[j][k] - 1] != y[j][k]:
                        flag = False

        if flag:
            ans = max(ans, honest.count(1))

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = [0] * N
    x = [[0] * N for i in range(N)]
    y = [[0] * N for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if y[j][k] == 1:
                        if not ((i >> (x[j][k] - 1)) & 1):
                            flag = False
                    else:
                        if (i >> (x[j][k] - 1)) & 1:
                            flag = False
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 9

def   main (): 
     N   =   int ( input ()) 
     A   =   [] 
     for   i   in   range ( N ): 
         A . append ( int ( input ())) 
         for   j   in   range ( A [ i ]): 
             x ,   y   =   map ( int ,   input (). split ()) 
     # print(N) 
     # print(A) 
     # print(x) 
     # print(y) 
     ans   =   0 
     for   i   in   range ( 2 ** N ): 
         # print(i) 
         honest   =   [ False ]   *   N 
         for   j   in   range ( N ): 
             if   ( i   >>   j )   &   1 : 
                 honest [ j ]   =   True 
         # print(honest) 
         flag   =   True 
         for   j   in   range ( N ): 
             if   honest [ j ]: 
                 for   k   in   range ( A [ j ]): 
                     x ,   y   =   map ( int ,   input (). split ()) 
                     if   y   ==   1   and   honest [ x - 1 ]   ==   False : 
                         flag   =   False 
                     if   y   ==   0   and   honest [ x - 1 ]: 
                         flag   =   False 
         if   flag : 
             ans   =   max ( ans ,   honest . count ( True )) 
     print ( ans )

=======
Suggestion 10

def main():
    N = int(input())
    #print(N)
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        #print(A[i])
        x = []
        y = []
        for j in range(A[i]):
            xj,yj = map(int,input().split())
            x.append(xj)
            y.append(yj)
        X.append(x)
        Y.append(y)
    #print(A)
    #print(X)
    #print(Y)
    ans = 0
    for i in range(2**N):
        bit = [0]*N
        for j in range(N):
            if (i>>j) & 1:
                bit[N-1-j] = 1
        #print(bit)
        flag = True
        for j in range(N):
            if bit[j] == 1:
                for k in range(A[j]):
                    if bit[X[j][k]-1] != Y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, sum(bit))
    print(ans)
