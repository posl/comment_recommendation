def main():
    a, b = map(int, input().split())
    if a == 0:
        print(0, 1)
        return
    if b == 0:
        print(1, 0)
        return
    if a == b:
        print(0.5, 0.5)
        return
    if a > b:
        print((a - b) / (2 * a), 0.5 + (a - b) / (2 * b))
        return
    if b > a:
        print(0.5 + (b - a) / (2 * a), (b - a) / (2 * b))
        return

if __name__ == '__main__':
    main()