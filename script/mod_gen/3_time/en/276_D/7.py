def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [1, 4, 3]
    # N = 3
    # A = [2, 7, 6]
    # N = 3
    # A = [1, 1, 1, 1, 1, 1]
    # N = 6
    A.sort()
    if A[0] != A[N-1]:
        print(-1)
        exit()
    count = 0
    for i in range(N):
        while A[i] % 2 == 0:
            count += 1
            A[i] = A[i] // 2
        while A[i] % 3 == 0:
            count += 1
            A[i] = A[i] // 3
    print(count)

if __name__ == '__main__':
    main()