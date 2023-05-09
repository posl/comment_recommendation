def main():
    N = int(input())
    A = list(map(int, input().split()))
    min_xor = 2**30
    for i in range(N):
        for j in range(i, N):
            xor = 0
            for k in range(i, j+1):
                xor = xor | A[k]
            min_xor = min(min_xor, xor)
    print(min_xor)

if __name__ == '__main__':
    main()