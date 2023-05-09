def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    m = x // d
    if m >= k:
        print(x - k * d)
    else:
        if (k - m) % 2 == 0:
            print(x - m * d)
        else:
            print(abs(x - (m + 1) * d))

if __name__ == '__main__':
    main()