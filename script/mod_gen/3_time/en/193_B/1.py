def main():
    N = int(input())
    A = [0] * N
    P = [0] * N
    X = [0] * N
    for i in range(N):
        A[i], P[i], X[i] = map(int, input().split())
    min_price = -1
    for i in range(N):
        if X[i] - A[i] > 0:
            if min_price == -1:
                min_price = P[i]
            else:
                min_price = min(min_price, P[i])
    print(min_price)
main()

if __name__ == '__main__':
    main()