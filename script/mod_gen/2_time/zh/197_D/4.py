def main():
    N = input()
    x0, y0 = map(int, input().split())
    xN, yN = map(int, input().split())
    x1 = (x0 + xN + (yN - y0) * 3 ** 0.5) / 2
    y1 = (y0 + yN + (x0 - xN) * 3 ** 0.5) / 2
    print(x1, y1)

if __name__ == '__main__':
    main()