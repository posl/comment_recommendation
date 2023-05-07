def main():
    x, y = map(int, input().split())
    if (x+y) % 3 != 0 or x+y < 3:
        print(0)
        exit()
    n = (x+y)//3
    a = min(x, y) - n + 1
    b = n - max(x, y) + 1
    print(comb(n, a) % (10**9+7))

if __name__ == '__main__':
    main()