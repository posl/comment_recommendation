def main():
    a, b, x = map(int, input().split())
    if a * 10 + b * 1 <= x:
        print(10**9)
        return
    if a * 1 + b * 1 > x:
        print(0)
        return
    if a * 1 + b * 10 > x:
        print(x // b)
        return
    if a * 1 + b * 10 <= x:
        print((x - a * 1) // b)
        return

if __name__ == '__main__':
    main()