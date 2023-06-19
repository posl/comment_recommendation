def main():
    N = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3 = (x1 + x2 + ((y2 - y1) * ((-1) ** (N / 2))) * (2 ** 0.5)) / 2
    y3 = (y1 + y2 + ((x1 - x2) * ((-1) ** (N / 2))) * (2 ** 0.5)) / 2
    print(x3, y3)

if __name__ == '__main__':
    main()