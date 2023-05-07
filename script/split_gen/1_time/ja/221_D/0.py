def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
    #print(A)
    #print(B)
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    #print(D)
    for i in range(N):
        D[i + 1] += D[i]
    #print(D)
    D = D[1:]
    #print(D)
    D = [str(x) for x in D]
    print(' '.join(D))
