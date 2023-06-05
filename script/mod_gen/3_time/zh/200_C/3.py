def problems200_c():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    D = {}
    for i in range(N):
        r = A[i] % 200
        if r in D:
            D[r] += 1
        else:
            D[r] = 1
    #print(D)
    ans = 0
    for k in D:
        if D[k] > 1:
            ans += D[k] * (D[k]-1) // 2
    print(ans)

if __name__ == '__main__':
    problems200_c()