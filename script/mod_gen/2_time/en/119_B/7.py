def main():
    N = int(input())
    total = 0
    for _ in range(N):
        x, u = input().split()
        if u == 'JPY':
            total += float(x)
        elif u == 'BTC':
            total += float(x) * 380000.0
    print(total)
main()

if __name__ == '__main__':
    main()