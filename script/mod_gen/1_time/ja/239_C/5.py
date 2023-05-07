def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3 = x2 - x1, y2 - y1
    x4, y4 = -y3, x3
    x5, y5 = x4 + x1, y4 + y1
    print('Yes' if x5 != x1 or y5 != y1 else 'No')
main()

if __name__ == '__main__':
    main()