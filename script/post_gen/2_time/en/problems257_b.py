Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    L = [int(x) for x in input().split()]
    B = [0] * N
    for i in range(K):
        B[A[i] - 1] = i + 1
    for i in range(Q):
        if B[L[i] - 1] > 0:
            if L[i] < N:
                if B[L[i]] == 0:
                    B[L[i] - 1] = 0
                    B[L[i]] = L[i]
                    L[i] += 1
            else:
                B[L[i] - 1] = 0
        else:
            pass
    for i in range(N):
        if B[i] > 0:
            print(B[i], end = " ")
        else:
            print(i + 1, end = " ")
    print()

=======
Suggestion 2

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * N
    for i in range(K):
        B[A[i] - 1] = i + 1
    for i in range(Q):
        if B[L[i] - 1] != 0:
            if L[i] != 1:
                B[L[i] - 2] = B[L[i] - 1]
                B[L[i] - 1] = 0
            else:
                B[L[i]] = B[L[i] - 1]
                B[L[i] - 1] = 0
    for i in range(N):
        if B[i] == 0:
            print(i + 1, end=" ")
        else:
            print(B[i], end=" ")
    print()

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * N
    for i in range(K):
        B[A[i]-1] = i+1
    for i in range(Q):
        if B[L[i]-1] != 0:
            B[L[i]-1], B[L[i]] = B[L[i]], B[L[i]-1]
    for i in range(N):
        if B[i] == 0:
            print(i+1, end=' ')
        else:
            print(A[B[i]-1], end=' ')

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #print(N, K, Q)
    #print(A)
    #print(L)
    B = [0] * (N+1)
    for i in range(K):
        B[A[i]] = i + 1
    #print(B)
    for i in range(Q):
        if B[L[i]] == 0:
            continue
        else:
            if B[L[i]] == 1:
                continue
            else:
                B[L[i]-1], B[L[i]] = B[L[i]], B[L[i]-1]
    for i in range(1, N+1):
        if B[i] == 0:
            print(i, end=" ")
        else:
            print(A[B[i]-1], end=" ")
    print()

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(K):
        B[A[i] - 1] = i + 1
    for i in range(Q):
        if B[L[i] - 1] == 0:
            continue
        else:
            if L[i] == 1:
                if B[L[i]] == 0:
                    B[L[i] - 1], B[L[i]] = B[L[i]], B[L[i] - 1]
            elif L[i] == N:
                if B[L[i] - 2] == 0:
                    B[L[i] - 1], B[L[i] - 2] = B[L[i] - 2], B[L[i] - 1]
            else:
                if B[L[i]] == 0:
                    B[L[i] - 1], B[L[i]] = B[L[i]], B[L[i] - 1]
                elif B[L[i] - 2] == 0:
                    B[L[i] - 1], B[L[i] - 2] = B[L[i] - 2], B[L[i] - 1]
    for i in range(N):
        if B[i] == 0:
            print(i + 1, end=' ')
        else:
            print(A[B[i] - 1], end=' ')

=======
Suggestion 6

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    B = [0] * N
    for i in range(K):
        B[A[i] - 1] = i + 1

    for i in range(Q):
        if B[L[i] - 1] != 0:
            if L[i] != 1 and B[L[i] - 2] == 0:
                B[L[i] - 2] = B[L[i] - 1]
                B[L[i] - 1] = 0
            elif L[i] != N and B[L[i]] == 0:
                B[L[i]] = B[L[i] - 1]
                B[L[i] - 1] = 0

    for i in range(N):
        if B[i] == 0:
            print(i + 1, end=' ')
        else:
            print(A[B[i] - 1], end=' ')

main()

=======
Suggestion 7

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        a[l[i] - 1] += 1
        if a[l[i] - 1] > n:
            a[l[i] - 1] = 1
        for j in range(k):
            if j != l[i] - 1:
                if a[j] == a[l[i] - 1]:
                    a[j] += 1
                    if a[j] > n:
                        a[j] = 1
    for i in range(k):
        print(a[i], end=' ')
    print()

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * (N + 2)
    for a in A:
        B[a] = 1
    for l in L:
        if B[A[l - 1] + 1] == 1:
            continue
        else:
            B[A[l - 1]] -= 1
            B[A[l - 1] + 1] += 1
            A[l - 1] += 1
    for i in range(1, N + 1):
        print(B[i], end=' ')

=======
Suggestion 9

def main():
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0]*n
    for i in range(k):
        b[a[i]-1] = i+1
    for i in range(q):
        if b[l[i]-1] != 0:
            b[l[i]-1],b[l[i]] = b[l[i]],b[l[i]-1]
    for i in range(n):
        print(b[i],end=' ')

=======
Suggestion 10

def main():
    #read input
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    
    #make a list of pieces
    pieces = [0] * n
    for i in range(k):
        pieces[a[i] - 1] = i + 1
    
    #process operations
    for i in range(q):
        #if the piece is on the rightmost square, do nothing
        if pieces[l[i] - 1] == 0:
            continue
        #if the piece is not on the rightmost square, move it one square right if there is no piece on the next square on the right
        else:
            #if the piece is on the rightmost square, do nothing
            if l[i] == n:
                continue
            #if the piece is not on the rightmost square, move it one square right if there is no piece on the next square on the right
            else:
                #if there is no piece on the next square on the right, move the piece one square right
                if pieces[l[i]] == 0:
                    pieces[l[i]] = pieces[l[i] - 1]
                    pieces[l[i] - 1] = 0
                #if there is a piece on the next square on the right, do nothing
                else:
                    continue
    
    #print the index of the square on which the i-th piece from the left is after the Q operations have ended
    for i in range(k):
        print(pieces.index(i + 1) + 1, end = " ")
