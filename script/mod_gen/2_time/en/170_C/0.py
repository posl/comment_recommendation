def main():
    X, N = map(int, input().split())
    p = set(map(int, input().split()))
    if N == 0:
        print(X)
    else:
        for i in range(0, 101):
            if X - i not in p:
                print(X - i)
                break
            elif X + i not in p:
                print(X + i)
                break

if __name__ == '__main__':
    main()