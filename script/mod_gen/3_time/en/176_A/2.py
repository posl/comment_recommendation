def main():
    N, X, T = map(int, input().split())
    time = 0
    if N % X == 0:
        time = (N // X) * T
    else:
        time = (N // X + 1) * T
    print(time)

if __name__ == '__main__':
    main()