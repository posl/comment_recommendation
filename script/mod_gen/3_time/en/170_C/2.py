def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(100):
        if X - i not in p:
            print(X - i)
            break
        elif X + i not in p:
            print(X + i)
            break

if __name__ == '__main__':
    main()