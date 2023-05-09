Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    count = 0
    for i in range(1, N+1):
        if i == X:
            break
        else:
            count += 1
            X = A[X]
    print(count)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    print(len(set(a)))

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    print(len([i for i in a if i > 0]))

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    friends = [0] * (n + 1)
    friends[x] = 1
    for i in range(1, n + 1):
        if friends[i] == 1:
            friends[a[i]] = 1
    print(sum(friends))

=======
Suggestion 5

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    count = 1
    for i in range(n):
        if i+1 == x:
            continue
        if a[i] == x:
            count += 1
            continue
        if a[a[i]-1] == x:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    friends = list(map(int, input().split()))
    friends[x-1] = 0
    for i in range(n):
        if friends[i] == x:
            friends[i] = 0
    print(len([i for i in friends if i != 0]))

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0,0)
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[i] = A[A[i]]
    C = [0] * (N + 1)
    for i in range(1, N + 1):
        C[i] = B[B[i]]
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = C[C[i]]
    E = [0] * (N + 1)
    for i in range(1, N + 1):
        E[i] = D[D[i]]
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = E[E[i]]
    G = [0] * (N + 1)
    for i in range(1, N + 1):
        G[i] = F[F[i]]
    H = [0] * (N + 1)
    for i in range(1, N + 1):
        H[i] = G[G[i]]
    I = [0] * (N + 1)
    for i in range(1, N + 1):
        I[i] = H[H[i]]
    J = [0] * (N + 1)
    for i in range(1, N + 1):
        J[i] = I[I[i]]
    K = [0] * (N + 1)
    for i in range(1, N + 1):
        K[i] = J[J[i]]
    L = [0] * (N + 1)
    for i in range(1, N + 1):
        L[i] = K[K[i]]
    M = [0] * (N + 1)
    for i in range(1, N + 1):
        M[i] = L[L[i]]
    N = [0] * (N + 1)
    for i in range(1, N + 1):
        N[i] = M[M[i]]
    O = [0] * (N + 1

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(X-1, 0)
    friends = [0] * N
    for i in range(N):
        friends[A[i]-1] += 1
    print(friends)
    print(max(friends))

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A = list(map(lambda x:x-1,A))
    A[X-1] = -1
    counter = 1
    for i in range(N):
        if A[i] == -1:
            continue
        else:
            counter += 1
            A[A[i]] = -1
    print(counter)

=======
Suggestion 10

def find_friends_with_secret(N, X, A):
    friends_with_secret = 1
    friend = X
    while True:
        friend = A[friend - 1]
        if friend == X:
            break
        friends_with_secret += 1
    return friends_with_secret
