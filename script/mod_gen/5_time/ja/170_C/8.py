def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = list(map(int, input().split()))
    p.sort()
    for i in range(0, 102):
        if (X - i) not in p:
            print(X - i)
            return
        if (X + i) not in p:
            print(X + i)
            return

if __name__ == '__main__':
    main()