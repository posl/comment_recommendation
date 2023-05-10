def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k*d <= x:
        print(x-k*d)
        return
    y = x // d
    if (k-y) % 2 == 0:
        print(x - y*d)
    else:
        print(abs(x-(y+1)*d))

if __name__ == '__main__':
    main()