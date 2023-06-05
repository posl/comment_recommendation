def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    m = min(k, x // d)
    k -= m
    x -= d * m
    if k % 2 == 0:
        print(x)
    else:
        print(abs(x - d))

if __name__ == '__main__':
    main()