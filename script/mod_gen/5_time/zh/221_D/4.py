def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A, B)
    C = [0] * (10**9 + 1)
    for i in range(N):
        C[A[i]] += 1
        C[A[i]+B[i]] -= 1
    #print(C)
    for i in range(1, 10**9 + 1):
        C[i] += C[i-1]
    #print(C)
    D = [0] * (N + 1)
    for i in range(1, 10**9 + 1):
        D[C[i]] += 1
    print(" ".join(map(str, D[1:])))
main()
