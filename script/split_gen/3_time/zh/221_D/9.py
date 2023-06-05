def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A, B)
    # D = [0] * N
    # for i in range(N):
    #     for j in range(A[i], A[i]+B[i]):
    #         D[j-1] += 1
    # print(D)
    # D = [0] * (10**9 + 1)
    # for i in range(N):
    #     for j in range(A[i], A[i]+B[i]):
    #         D[j] += 1
    # print(D)
    # D = [0] * (10**9 + 1)
    # for i in range(N):
    #     D[A[i]] += 1
    #     D[A[i]+B[i]] -= 1
    # print(D)
    # D = [0] * (10**9 + 1)
    # for i in range(N):
    #     D[A[i]] += 1
    #     D[A[i]+B[i]] -= 1
    # for i in range(1, 10**9+1):
    #     D[i] += D[i-1]
    # print(D)
    D = [0] * (10**9 + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i]+B[i]] -= 1
    for i in range(1, 10**9+1):
        D[i] += D[i-1]
    print(*D[1:])
