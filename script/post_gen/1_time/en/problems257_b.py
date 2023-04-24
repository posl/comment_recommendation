Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        a[l[i] - 1] += 1
    for j in range(k):
        if a[j] - q > 0:
            print(j + 1)

=======
Suggestion 2

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        a[l[i] - 1] += 1
    for i in range(k):
        if a[i] - q - 1 > 0:
            print(a[i] - q - 1, end=' ')
        else:
            print('0', end=' ')

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    ans = [0] * K
    for i in range(K):
        ans[i] = A[i]

    for i in range(Q):
        if ans[L[i] - 1] != N:
            ans[L[i] - 1] += 1

    for i in range(K):
        print(ans[i], end=' ')

=======
Suggestion 4

def main():
    # input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # compute
    B = [0]*N
    for i in A:
        B[i-1] = 1
    for i in L:
        if B[A[i-1]-1] == 1:
            if A[i-1] < N:
                if B[A[i-1]] == 0:
                    B[A[i-1]-1] = 0
                    B[A[i-1]] = 1
                    A[i-1] += 1
            else:
                B[A[i-1]-1] = 0
                B[0] = 1
                A[i-1] = 1

    # output
    for i in range(N):
        if B[i] == 1:
            print(i+1, end=' ')

main()

=======
Suggestion 5

def solve():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #print(N, K, Q)
    #print(A)
    #print(L)
    B = [0] * N
    for i in range(K):
        B[A[i] - 1] = i + 1
    #print(B)
    for i in range(Q):
        l = L[i] - 1
        if B[l] == 0:
            continue
        if l == 0:
            if B[l + 1] == 0:
                B[l], B[l + 1] = B[l + 1], B[l]
        elif l == N - 1:
            if B[l - 1] == 0:
                B[l], B[l - 1] = B[l - 1], B[l]
        else:
            if B[l - 1] == 0:
                B[l], B[l - 1] = B[l - 1], B[l]
            elif B[l + 1] == 0:
                B[l], B[l + 1] = B[l + 1], B[l]
    for i in range(N):
        if B[i] == 0:
            continue
        else:
            print(i + 1, end = ' ')
    print()

=======
Suggestion 6

def main():
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    l=list(map(int,input().split()))
    p=[0 for i in range(n)]
    for i in range(k):
        p[a[i]-1]=i+1
    for i in range(q):
        if p[l[i]-1]!=0:
            if l[i]!=1:
                if p[l[i]-2]==0:
                    p[l[i]-2]=p[l[i]-1]
                    p[l[i]-1]=0
            if l[i]!=n:
                if p[l[i]]==0:
                    p[l[i]]=p[l[i]-1]
                    p[l[i]-1]=0
    for i in range(n):
        print(p[i],end=' ')

=======
Suggestion 7

def main():
    #input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #output
    print(*[A[i-1]+L[j]-1 for j,i in enumerate(L)])

=======
Suggestion 8

def main():
    # Read input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # Solve
    B = [0] * N
    for i in range(K):
        B[A[i]-1] = i+1
    for i in range(Q):
        if B[L[i]-1] == 0:
            continue
        if L[i] == N:
            continue
        if B[L[i]] != 0:
            continue
        B[L[i]-1], B[L[i]] = B[L[i]], B[L[i]-1]
    # Print output
    for i in range(N):
        print(B[i], end=' ')
    print()

=======
Suggestion 9

def main():
    # Read input
    # Read N, K, and Q
    N, K, Q = map(int, input().split())
    # Read A_1, A_2, ..., A_K
    A = list(map(int, input().split()))
    # Read L_1, L_2, ..., L_Q
    L = list(map(int, input().split()))
    
    # Initialize the list of squares
    squares = [0] * N
    
    # Place the pieces on the squares
    for i in range(K):
        squares[A[i]-1] = i+1
    
    # Perform the operations
    for i in range(Q):
        # Get the index of the piece
        piece = L[i] - 1
        # Get the index of the square where the piece is
        square = A[piece] - 1
        # If the piece is on its rightmost square, do nothing
        if square == N-1:
            continue
        # If the next square on the right does not contain a piece, move the piece
        if squares[square+1] == 0:
            squares[square] = 0
            squares[square+1] = piece+1
            A[piece] += 1
    
    # Print the indices of the squares on which the pieces are
    print(*[A[i] for i in range(K)])

=======
Suggestion 10

def print_list(list):
    print(" ".join([str(i) for i in list]))
