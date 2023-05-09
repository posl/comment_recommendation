def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    print(P.index(X) + 1)

if __name__ == '__main__':
    main()