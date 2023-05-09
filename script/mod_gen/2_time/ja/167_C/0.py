def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_price = float("inf")
    for i in range(2**N):
        price = 0
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1 == 1:
                price += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            min_price = min(min_price, price)
    if min_price == float("inf"):
        print(-1)
    else:
        print(min_price)

if __name__ == '__main__':
    main()