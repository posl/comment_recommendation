def main():
    N = int(input())
    min_price = 10 ** 9 + 1
    for _ in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0 and P < min_price:
            min_price = P
    if min_price == 10 ** 9 + 1:
        print(-1)
    else:
        print(min_price)
main()

if __name__ == '__main__':
    main()