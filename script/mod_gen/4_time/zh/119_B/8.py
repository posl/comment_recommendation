def main():
    n = int(input())
    result = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            result += float(x) * 380000
        else:
            result += int(x)
    print(result)

if __name__ == '__main__':
    main()