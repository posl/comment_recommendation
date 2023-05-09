def main():
    n = int(input())
    y = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            y += float(x) * 380000
        else:
            y += int(x)
    print(y)

if __name__ == '__main__':
    main()