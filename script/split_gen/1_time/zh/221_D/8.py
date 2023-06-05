def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N)
    #print(A)
    #print(B)
    #print("----")
    C = [0]*(10**9+2)
    for i in range(N):
        C[A[i]] += 1
        C[A[i]+B[i]] -= 1
    #print(C)
    #print("----")
    D = [0]*(N+1)
    for i in range(1, 10**9+2):
        C[i] += C[i-1]
        if C[i] <= N:
            D[C[i]] += 1
    #print(D)
    #print("----")
    for i in range(1, N+1):
        print(D[i], end=" ")
    print()
