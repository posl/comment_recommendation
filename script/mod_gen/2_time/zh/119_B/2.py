def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        if u == "BTC":
            total += float(x)*380000.0
        else:
            total += int(x)
    print(total)

if __name__ == '__main__':
    main()