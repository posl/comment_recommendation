def main():
    x1, y1, x2, y2 = map(int, input().split())
    print('Yes' if abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 == 5 else 'No')

if __name__ == '__main__':
    main()