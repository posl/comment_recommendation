def main():
    X = input()
    M = int(input())
    d = int(max(X))
    n = d + 1
    while int(X, n) <= M:
        n += 1
    print(n-d-1)

if __name__ == '__main__':
    main()