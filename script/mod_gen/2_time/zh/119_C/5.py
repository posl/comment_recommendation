def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            sum += float(x) * 380000
        else:
            sum += float(x)
    print(sum)

if __name__ == '__main__':
    main()