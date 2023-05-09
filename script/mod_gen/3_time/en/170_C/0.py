def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    p = set(map(int, input().split()))
    for i in range(101):
        if X - i not in p:
            print(X - i)
            return
        if X + i not in p:
            print(X + i)
            return

if __name__ == '__main__':
    main()