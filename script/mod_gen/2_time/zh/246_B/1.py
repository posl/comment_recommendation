def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    print(x1 + x3 - x2, y1 + y3 - y2)

if __name__ == '__main__':
    main()