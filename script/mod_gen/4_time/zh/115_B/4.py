def main():
    n = int(input())
    price = []
    for i in range(n):
        price.append(int(input()))
    price.sort(reverse=True)
    price[0] = price[0] / 2
    print(int(sum(price)))

if __name__ == '__main__':
    main()