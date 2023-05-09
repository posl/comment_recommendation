def main():
    r, x, y = map(int, input().split())
    if r * r == x * x + y * y:
        print(1)
    elif r * r > x * x + y * y:
        print(2)
    else:
        print((x * x + y * y + r * r - 1) // (r * r))

if __name__ == '__main__':
    main()