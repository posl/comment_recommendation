def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    n = (x + y) // 3
    if x < n or y < n:
        print(0)
        return
    print(comb(n + x - n, x - n))

if __name__ == '__main__':
    main()