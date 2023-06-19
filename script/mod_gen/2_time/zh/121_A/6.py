def main():
    h, w = map(int, input().split())
    a, b = map(int, input().split())
    print((h - a) * (w - b))

if __name__ == '__main__':
    main()