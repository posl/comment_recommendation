def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
    else:
        m = x // d
        if (k - m) % 2 == 0:
            print(x - m * d)
        else:
            print(d - x + m * d)

if __name__ == '__main__':
    main()