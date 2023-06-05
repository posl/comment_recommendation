def main():
    h, w = map(int, input().split())
    a, b = map(int, input().split())
    print(h * w - (a * w + b * (h - a)))

if __name__ == '__main__':
    main()