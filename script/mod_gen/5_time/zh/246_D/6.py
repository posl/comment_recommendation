def main():
    N = int(input())
    X = N
    while True:
        if X >= N and (X ** (1/3)).is_integer():
            print(X)
            break
        X += 1

if __name__ == '__main__':
    main()