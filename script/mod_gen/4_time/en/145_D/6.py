def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
    else:
        n = (x + y) // 3
        if x < n or y < n:
            print(0)
        else:
            print(comb(x, y, n))

if __name__ == '__main__':
    main()