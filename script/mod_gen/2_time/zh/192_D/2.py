def main():
    X = input()
    M = int(input())
    d = int(max(X))
    n = d + 1
    X = int(X)
    count = 0
    while True:
        if X == 0:
            break
        count += 1
        X //= n
    print(count)

if __name__ == '__main__':
    main()