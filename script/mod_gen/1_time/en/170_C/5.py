def main():
    X, N = map(int, input().split())
    P = set(map(int, input().split()))
    if N == 0:
        print(X)
        return
    for i in range(100):
        if X - i not in P:
            print(X - i)
            return
        if X + i not in P:
            print(X + i)
            return
main()

if __name__ == '__main__':
    main()