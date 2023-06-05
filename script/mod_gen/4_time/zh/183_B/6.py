def main():
    s = input()
    x1, y1, x2, y2 = map(int, s.split())
    x = (x2 * y1 + x1 * y2) / (y1 + y2)
    print(x)

if __name__ == '__main__':
    main()