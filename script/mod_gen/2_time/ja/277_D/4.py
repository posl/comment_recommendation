def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    ans = 0
    for i in range(N):
        ans += A[i]
    #print(ans)
    if ans == 0:
        print(0)
        exit()
    if ans % M == 0:
        print(0)
        exit()
    if ans % M != 0:
        for i in range(N):
            if A[i] % M == 0:
                print(ans)
                exit()
            if A[i] % M != 0:
                if ans - A[i] + (A[i] + 1) % M <= ans:
                    ans = ans - A[i] + (A[i] + 1) % M
                else:
                    continue
        print(ans)
        exit()

if __name__ == '__main__':
    main()