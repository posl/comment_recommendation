def main():
    N, K = map(int, input().split())
    price = list(map(int, input().split()))
    price.sort()
    print(sum(price[:K]))

if __name__ == '__main__':
    main()