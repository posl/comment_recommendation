def main():
    # input
    n, x, t = map(int, input().split())
    # compute
    time = 0
    if n % x == 0:
        time = n // x * t
    else:
        time = n // x * t + t
    # output
    print(time)

if __name__ == '__main__':
    main()