Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in range(Q):
        print(N - bisect.bisect_right(A, x[i]))

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(N - bisect.bisect_right(A, x))

=======
Suggestion 3

def main():
    import bisect
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in x:
        print(bisect.bisect_left(A, i))

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in x:
        print(n - bisect.bisect_right(a, i - 1))

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]

    A.sort()

    for j in range(Q):
        left = 0
        right = N
        while right - left > 1:
            mid = (left + right) // 2
            if A[mid] >= x[j]:
                right = mid
            else:
                left = mid
        print(N - right + 1)

=======
Suggestion 6

def main():
    #input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    #solve
    A.sort()
    for x in X:
        print(N - bisect.bisect_right(A, x))

=======
Suggestion 7

def main():
    import sys
    from bisect import bisect_right
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(bisect_right(A, x))

=======
Suggestion 8

def main():
    #input
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    xs = [int(input()) for _ in range(Q)]

    #process
    As.sort()
    As = [0] + As
    for i in range(N):
        As[i+1] += As[i]
    for x in xs:
        #binary search
        ng = -1
        ok = N+1
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if As[mid] >= x*(N-mid+1):
                ok = mid
            else:
                ng = mid
        print(N-ok+1)

=======
Suggestion 9

def  main ( ) :
    # read the number of students and the number of queries
     n ,  q  =  map ( int ,  input ( ) . split ( ) )
    # read the heights of students
     a  =  list ( map ( int ,  input ( ) . split ( ) ) )
    # read the queries
     x  = [ int ( input ( ) )  for  _  in  range ( q ) ]

    # sort the heights in ascending order
     a . sort ( )

    # find the index of the first student with a height of at least x_j
     # by using binary search
     for  j  in  range ( q ) :
        print ( bisect . bisect_left ( a ,  x [ j ] ) )
