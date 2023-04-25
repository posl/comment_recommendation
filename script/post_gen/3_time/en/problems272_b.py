Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    K = [0] * M
    X = [0] * M
    for i in range(M):
        K[i], *X[i] = map(int, input().split())
    for i in range(M):
        for j in range(i + 1, M):
            if len(set(X[i]) & set(X[j])) == 0:
                print('No')
                return
    print('Yes')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    parties = [set(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            if not any(i + 1 in party and j + 1 in party for party in parties):
                print("No")
                return
    print("Yes")

main()

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    d = [0] * n
    for _ in range(m):
        k, *x = map(int, input().split())
        for i in range(k):
            d[x[i] - 1] += 1
    print('Yes' if all(x > 0 for x in d) else 'No')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        A.append(list(map(int, input().split())))
    B = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        for j in range(A[i][0]):
            for k in range(j+1, A[i][0]):
                B[A[i][j+1]-1][A[i][k+1]-1] = 1
                B[A[i][k+1]-1][A[i][j+1]-1] = 1
    for i in range(N):
        for j in range(N):
            if B[i][j] == 0:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    for i in range(M):
        k,*x = map(int,input().split())
        for j in range(k):
            for l in range(j+1,k):
                if x[j] == x[l]:
                    print("No")
                    exit()
    print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [0] * N
    for _ in range(M):
        *B, = map(int, input().split())
        for i in range(1, B[0]+1):
            A[B[i]-1] += 1
    if 0 in A:
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    for i in range(M):
        input()
    print("Yes")

=======
Suggestion 8

def main():
    # Read the data
    N, M = map(int, input().split())
    k = [0] * M
    x = [[0] * N for i in range(M)]
    for i in range(M):
        k[i], *x[i] = map(int, input().split())
    #print(N, M, k, x)

    # Solve the problem
    # Initialize the array
    attended = [[0] * N for i in range(N)]
    #print(attended)

    # Fill the array
    for i in range(M):
        for j in range(k[i]):
            for l in range(k[i]):
                attended[x[i][j] - 1][x[i][l] - 1] = 1
    #print(attended)

    # Check if the array is filled
    for i in range(N):
        for j in range(N):
            if attended[i][j] == 0:
                print("No")
                return

    # Print the answer
    print("Yes")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    for i in range(M):
        k, *x = map(int, input().split())
        if k == 1:
            if len(x) != 1:
                print("No")
                return
        elif k == 2:
            if x[0] == x[1]:
                print("No")
                return
        else:
            if x[0] == x[1] or x[1] == x[2]:
                print("No")
                return
    print("Yes")

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    for _ in range(M):
        input()
    if N == M:
        print("Yes")
    else:
        print("No")
