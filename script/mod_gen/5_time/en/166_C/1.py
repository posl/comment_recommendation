def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, M, H, A, B)
    #print(N, M, H, A, B)
    good = [True for i in range(N)]
    for i in range(M):
        if H[A[i]-1] <= H[B[i]-1]:
            good[A[i]-1] = False
        if H[A[i]-1] >= H[B[i]-1]:
            good[B[i]-1] = False
    #print(good)
    print(good.count(True))
main()
