Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     A   =   [ a   for   a   in   A   if   a   >   0 ] 
     N   =   len ( A ) 
     A   =   [ a   -   1   for   a   in   A ] 
     A   =   sorted ( A ) 
     A   =   [ a   +   1   for   a   in   A ] 
     A   =   [ a   -   1   for   a   in   A ] 

     # print(A) 
     # print(N) 

     #

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = [0] * N
    for i in range(N):
        C[i] = B.index(A[i])
    D = [0] * N
    for i in range(N):
        D[C[i]] += 1
    E = [0] * N
    for i in range(N):
        E[i] = D[i] * (D[i] - 1) // 2
    F = [0] * N
    for i in range(N):
        F[C[i]] += 1
        if i != 0:
            F[i] += F[i - 1]
    G = [0] * N
    for i in range(N):
        G[i] = F[i] * (F[i] - 1) // 2
    for i in range(N):
        print(G[i] - E[i])

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = list(enumerate(A))
    A.sort(key=lambda x: x[1])
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[i] = N - 1
        else:
            ans[i] = ans[i - 1] - 1
    for i in range(N):
        ans[A[i][0]] = ans[i]
    for a in ans:
        print(a)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = sorted(A)
    C = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = C[i] + B[i]
    for i in range(N):
        idx = B.index(A[i])
        print(N - idx - (C[N] - C[idx + 1]) + A[i])

main()

=======
Suggestion 5

def   main ():
     n   =   int ( input ())
     a   =   list ( map ( int ,   input (). split ()))
     b   =   [ 0 ]* n
     c   =   [ 0 ]* n
     for   i   in   range ( n ):
         b [ i ]   =   [ a [ i ],   i ]
     b . sort ()
     for   i   in   range ( n ):
         c [ b [ i ][ 1 ]]   =   i 
     d   =   [ 0 ]* n 
     for   i   in   range ( n ):
         d [ c [ i ]]   +=   1 
     e   =   [ 0 ]* n 
     for   i   in   range ( n ):
         e [ i ]   =   e [ i - 1 ]   +   d [ i ]
     f   =   [ 0 ]* n 
     for   i   in   range ( n ):
         f [ i ]   =   e [ i ]   -   e [ c [ i ]]
     for   i   in   range ( n ):
         print ( f [ i ])

=======
Suggestion 6

def main():
    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    S = sorted(C.items(), key=lambda x: x[0])
    T = [0]
    for i in range(len(S)):
        T.append(T[i] + S[i][1])
    for i in range(N):
        print(T[bisect.bisect_left(S, (A[i], 0))] + N - T[bisect.bisect_right(S, (A[i], 10**9))])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A[64])
    #print(A[65])
    #print(A[66])
    #

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(set(a))
    a.sort()
    if len(a) == 1:
        print(n)
        return
    ans = [0] * n
    for i in range(len(a) - 1):
        ans[i] = n - (len(a) - i)
    ans[len(a) - 1] = 1
    print('

'.join(map(str, ans)))

=======
Suggestion 9

def main():
    #input
    n = int(input())
    a = list(map(int,input().split()))

    #count
    count = [0] * (10**9+1)
    for i in range(n):
        count[a[i]] += 1

    #cumsum
    cumsum = [0] * (10**9+1)
    for i in range(10**9+1):
        cumsum[i] = cumsum[i-1] + count[i]

    #solve
    for i in range(n):
        print(n - cumsum[a[i]])

=======
Suggestion 10

def count_greater_than_Ai(A, N):
    A.sort()
    A.append(0)
    greater_than_Ai = 1
    count_greater_than_Ai = []
    for i in range(1, N+1):
        if A[i] != A[i-1]:
            count_greater_than_Ai.append(greater_than_Ai)
            greater_than_Ai = 1
        else:
            greater_than_Ai += 1
    return count_greater_than_Ai
