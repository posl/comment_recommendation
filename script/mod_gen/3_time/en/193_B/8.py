def main():
    N = int(input())
    min_price = 10**9 + 1
    for i in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            min_price = min(min_price, P)
    print(min_price if min_price < 10**9 + 1 else -1)

if __name__ == '__main__':
    main()