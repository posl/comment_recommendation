def main():
    X = int(input())
    M = int(input())
    if M < X:
        print(0)
        return
    if X < 10:
        print(1)
        return
    X = str(X)
    d = max(X)
    n = int(d) + 1
    while True:
        if n * (n - 1) ** (len(X) - 1) > M:
            break
        n += 1
    print(n - d - 1)
main()

if __name__ == '__main__':
    main()