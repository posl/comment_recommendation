def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                if i == N - 1 and A[i] == A[0]:
                    print(count)
                    return
                else:
                    print(-1)
                    return
        count += 1

if __name__ == '__main__':
    main()