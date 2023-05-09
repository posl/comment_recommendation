def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
    else:
        prod = 1
        for i in range(N):
            prod *= A[i]
            if prod > 10 ** 18:
                print(-1)
                exit()
        print(prod)

if __name__ == '__main__':
    main()