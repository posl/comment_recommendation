def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                if A.count(A[i]) == N:
                    print(cnt)
                    return
                else:
                    print(-1)
                    return
        cnt += 1

if __name__ == '__main__':
    main()