def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            elif A[i] % 3 == 0:
                A[i] //= 3
            else:
                print(count)
                exit()
        count += 1
    print(-1)

if __name__ == '__main__':
    main()