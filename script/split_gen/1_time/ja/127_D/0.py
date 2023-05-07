def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)
    #print(C)
    A.sort(reverse=True)
    C.sort(reverse=True)
    #print(A)
    #print(C)
    ans = 0
    j = 0
    for i in range(N):
        if j < M and A[i] < C[j]:
            ans += C[j]
            B[j] -= 1
            if B[j] == 0:
                j += 1
        else:
            ans += A[i]
    print(ans)
