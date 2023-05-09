def main():
    X, K = [int(x) for x in input().split()]
    for i in range(1, K+1):
        X = round(X, -i)
    print(X)

if __name__ == '__main__':
    main()