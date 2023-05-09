def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j]-1 == i:
                if H[i] <= H[B[j]-1]:
                    flag = False
                    break
            if B[j]-1 == i:
                if H[i] <= H[A[j]-1]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()