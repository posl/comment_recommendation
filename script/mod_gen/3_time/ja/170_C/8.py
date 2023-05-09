def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    if N == 0:
        print(X)
        return
    p.sort()
    print(p)
    for i in range(0, 101):
        if X - i not in p:
            print(X - i)
            return
        elif X + i not in p:
            print(X + i)
            return

if __name__ == '__main__':
    main()