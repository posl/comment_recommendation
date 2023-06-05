def main():
    n = int(input())
    price = []
    for i in range(n):
        price.append(int(input()))
    price.sort()
    price[n-1] = price[n-1] / 2
    print(int(sum(price)))

if __name__ == '__main__':
    main()