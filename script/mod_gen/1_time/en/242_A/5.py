def main():
    a, b, c, x = map(int, input().split())
    t = 0
    if x <= a:
        t = 1
    elif a < x <= b:
        t = ((b - x + 1) / (b - a + 1)) * ((c - 1) / (b - a))
    print(t)

if __name__ == '__main__':
    main()