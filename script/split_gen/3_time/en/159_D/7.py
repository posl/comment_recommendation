def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i]] += 1
    #print(B)
    #print(sum(B))
    C = [0] * (N + 1)
    for i in range(N + 1):
        C[i] = B[i] * (B[i] - 1) // 2
    #print(C)
    D = sum(C)
    #print(D)
    for i in range(N):
        print(D - C[A[i]] + (B[A[i]] - 1) * (B[A[i]] - 2) // 2)
