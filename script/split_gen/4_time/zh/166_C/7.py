def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M)
    #print(H)
    #print(A)
    #print(B)
    #print("----------")
    #print(N, M, H, A, B)
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            #print(i, j)
            #print(H[A[j]-1], H[B[j]-1])
            if H[A[j]-1] >= H[B[j]-1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
