def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    x1 = (x0 + xN2)/2 - ((y0 - yN2)/2)/tan(radians(180/n))
    y1 = (y0 + yN2)/2 + ((x0 - xN2)/2)/tan(radians(180/n))
    print(x1, y1)

if __name__ == '__main__':
    main()