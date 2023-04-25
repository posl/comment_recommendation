Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     N ,   K   =   map ( int ,   input (). split ()) 
     A   =   [ list ( map ( int ,   input (). split ()))   for   _   in   range ( N )] 
     A   =   [ [ 0 ]   +   a   +   [ 0 ]   for   a   in   A ] 
     A . insert ( 0 ,   [ 0 ]   *   ( N   +   2 )) 
     A . append ( [ 0 ]   *   ( N   +   2 )) 

     for   i   in   range ( N ): 
         for   j   in   range ( N ): 
             A [ i   +   1 ][ j   +   1 ]   +=   A [ i   +   1 ][ j ]   +   A [ i ][ j   +   1 ]   -   A [ i ][ j ] 

     def   check ( x ): 
         for   i   in   range ( N   -   K   +   1 ): 
             for   j   in   range ( N   -   K   +   1 ): 
                 if   A [ i   +   K ][ j   +   K ]   -   A [ i   +   K ][ j ]   -   A [ i ][ j   +   K ]   +   A [ i ][ j ]   <   K   *   K   *   x : 
                     return   True 
         return   False 

     left   =   0 
     right   =   10 ** 9 
     while   right   -   left   >   1 : 
         mid   =   ( left   +   right )   //   2 
         if   check ( mid ): 
             right   =   mid 
         else : 
             left   =   mid 
     print ( right )

=======
Suggestion 2

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

N,K = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

min = 10**9+1
for i in range(N-K+1):
    for j in range(N-K+1):
        lst = []
        for k in range(K):
            for l in range(K):
                lst.append(A[i+k][j+l])
        med = median(lst)
        if med < min:
            min = med

print(int(min))

I have an array of arrays of integers, and I want to find the median of each array. This is my code:

=======
Suggestion 3

def   main ( ) : 
     N ,   K   =   map ( int ,   input ( ) . split ( ) ) 
     A   =   [ list ( map ( int ,   input ( ) . split ( ) ) )   for   _   in   range ( N ) ] 
     B   =   [ [ 0 ]   *   ( N + 1 )   for   _   in   range ( N + 1 ) ] 
     for   i   in   range ( N ) : 
         for   j   in   range ( N ) : 
             B [ i + 1 ] [ j + 1 ]   =   A [ i ] [ j ]   +   B [ i ] [ j + 1 ]   +   B [ i + 1 ] [ j ]   -   B [ i ] [ j ] 
     def   check ( x ) : 
         for   i   in   range ( N - K + 1 ) : 
             for   j   in   range ( N - K + 1 ) : 
                 if   B [ i + K ] [ j + K ]   +   B [ i ] [ j ]   -   B [ i + K ] [ j ]   -   B [ i ] [ j + K ]   <   K * K * x : 
                     return   True 
         return   False 
     ok   =   10 ** 9 
     ng   =   0 
     while   ok   -   ng   >   1 : 
         mid   =   ( ok   +   ng )   //   2 
         if   check ( mid ) : 
             ok   =   mid 
         else : 
             ng   =   mid 
     print ( ok )

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    l, r = 0, 10**9
    while r-l > 1:
        m = (l+r)//2
        if check(A, K, m):
            r = m
        else:
            l = m
    print(r)

=======
Suggestion 5

def check(mid):
    for i in range(N-K+1):
        for j in range(N-K+1):
            if A[i][j] <= mid <= A[i+K-1][j+K-1]:
                return True
    return False

N, K = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(N)]
A.sort()
A = [[A[i][j] for j in range(N)] for i in range(N)]
A.sort(key=lambda x: x[0])
ok = 10**9 + 1
ng = -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)

The first half of the code is the same as the previous one. The second half is to perform binary search on the answer. In the binary search, we can check if the median is ok or not by the following function.

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    a.sort(key=lambda x: x[1])
    a.sort(key=lambda x: x[0])
    ans = 10 ** 9
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            b = []
            for l in range(k):
                b += a[i + l][j:j + k]
            b.sort()
            ans = min(ans, b[k * k // 2])
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = [[int(i) for i in input().split()] for j in range(N)]
    B = [0] * (N * N)
    cnt = 0
    for i in range(N):
        for j in range(N):
            B[cnt] = A[i][j]
            cnt += 1
    B.sort()
    l = 0
    r = N * N
    while l + 1 < r:
        mid = (l + r) // 2
        if check(A, B[mid], N, K):
            r = mid
        else:
            l = mid
    print(B[r])

=======
Suggestion 8

def main():
    #N: number of rows
    #K: number of columns
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(A)
    #print(N, K)

    #list of median of heights of squares
    median_list = []

    #find median of heights of squares
    for i in range(0, N - K + 1):
        for j in range(0, N - K + 1):
            #print("i = ", i, "j = ", j)
            #print("A[i][j] = ", A[i][j])
            #print("A[i][j+K-1] = ", A[i][j+K-1])
            #print("A[i+K-1][j] = ", A[i+K-1][j])
            #print("A[i+K-1][j+K-1] = ", A[i+K-1][j+K-1])
            median = A[i][j] + A[i+K-1][j+K-1] - A[i+K-1][j] - A[i][j+K-1]
            #print("median = ", median)
            median_list.append(median)

    #print("median_list = ", median_list)
    print(min(median_list))

=======
Suggestion 9

def main():
    #N: park's size, K: pond's size
    N, K = map(int, input().split())
    #A: park's height
    A = [list(map(int, input().split())) for _ in range(N)]
    #B: cumulative sum of A
    B = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j] + A[i][j]
    
    #binary search
    #l: min height, r: max height
    l, r = 0, 10 ** 9
    while r - l > 1:
        m = (l + r) // 2
        #check if there's a pond with median height >= m
        if check(B, N, K, m):
            l = m
        else:
            r = m
    print(l)

=======
Suggestion 10

def check ( k , a , mid ): #check if the median of the heights of the squares in a k*k section is lower than or equal to mid. n = len ( a ) for i in range ( n - k + 1 ): for j in range ( n - k + 1 ): cnt = 0 for x in range ( k ): for y in range ( k ): if a [ i + x ][ j + y ] <= mid : cnt += 1 if cnt > k * k // 2 : return True return False n , k = map ( int , input (). split ()) a = [ list ( map ( int , input (). split ())) for _ in range ( n )] ok = 0 #ok is the lower bound of the answer. ng = 10 ** 9 + 1 #ng is the upper bound of the answer. while ng - ok > 1 : mid = ( ok + ng ) // 2 if check ( k , a , mid ): ng = mid else : ok = mid print ( ng )
