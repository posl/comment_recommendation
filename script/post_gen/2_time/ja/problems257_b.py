Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * N
    for i in range(K):
        B[A[i] - 1] = i + 1
    for i in range(Q):
        if B[L[i] - 1] != 0:
            if L[i] != K:
                if B[L[i]] == 0:
                    B[L[i]] = B[L[i] - 1]
                    B[L[i] - 1] = 0
            L[i] += 1
    for i in range(N):
        if B[i] != 0:
            print(B[i], end=' ')

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
        if L[i] == K:
            continue
        if B[L[i]] != 0 and B[L[i] - 1] == 0:
            B[L[i] - 1] = B[L[i]]
            B[L[i]] = 0
    print(*B)

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
            if B[L[i]-1] == N:
                pass
            elif B[L[i]] == 0:
                B[L[i]-1], B[L[i]] = B[L[i]], B[L[i]-1]
    for i in range(N):
        if B[i] != 0:
            print(B[i], end = " ")

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * N
    for i in range(K):
        B[A[i]-1] = i+1
    for i in range(Q):
        if L[i] == 1:
            if B[0] != 0:
                if B[1] == 0:
                    B[0], B[1] = B[1], B[0]
        else:
            for j in range(N-1):
                if B[j] == L[i]:
                    if B[j+1] == 0:
                        B[j], B[j+1] = B[j+1], B[j]
    for i in range(K):
        print(B.index(i+1)+1, end=" ")

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #print(N, K, Q)
    #print(A)
    #print(L)
    #print("")

    #init
    B = [0] * (N+1)
    for i in range(K):
        B[A[i]] = 1

    #print(B)

    for i in range(Q):
        #print(i, L[i])
        if B[L[i]] == 1:
            #print("B[L[i]] == 1")
            if L[i] == N:
                #print("L[i] == N")
                pass
            else:
                if B[L[i]+1] == 0:
                    #print("B[L[i]+1] == 0")
                    B[L[i]] = 0
                    B[L[i]+1] = 1
        else:
            #print("B[L[i]] == 0")
            pass
        #print(B)

    for i in range(1, N+1):
        if B[i] == 1:
            print(i, end=" ")
    print("")

=======
Suggestion 6

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i] - 1] = i + 1
    for i in range(q):
        if b[l[i] - 1] != 0:
            if b[l[i] - 1] == k:
                b[l[i] - 1] = 0
            else:
                b[l[i] - 1] = b[l[i] - 1] + 1
    for i in range(n):
        if b[i] != 0:
            print(b[i], end=' ')
        else:
            print(0, end=' ')

=======
Suggestion 7

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for i in range(Q):
        if A[L[i]-1] < N:
            if A[L[i]] != A[L[i]-1] + 1:
                A[L[i]] += 1
                A[L[i]-1] += 1
    for i in range(K):
        print(A[i], end=" ")
    print()

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    pos = [0] * (N+1)
    for i in range(K):
        pos[A[i]] = i+1
    for i in L:
        if pos.index(i) == N:
            continue
        elif pos[pos.index(i)+1] == 0:
            pos[pos.index(i)] = 0
            pos[pos.index(i)+1] = i
        else:
            continue
    for i in range(1, N+1):
        if pos[i] == 0:
            print(i, end=' ')
        else:
            print(pos.index(pos[i]), end=' ')

=======
Suggestion 9

def main():
    # 入力
    N,K,Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # 処理
    B = [0]*N
    for i in range(K):
        B[A[i]-1] = i+1
    for i in range(Q):
        if B[L[i]-1] != 0 and L[i] < K:
            B[L[i]-1], B[L[i]] = B[L[i]], B[L[i]-1]
    # 出力
    for i in range(N):
        if B[i] == 0:
            print(i+1, end=" ")
        else:
            print(B[i], end=" ")
    print()
