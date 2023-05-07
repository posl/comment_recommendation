def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        print(abs(x - a))
        return
    if a <= x <= a + (n - 1) * d:
        print(0)
        return
    if x < a:
        print(min(abs(x - a), abs(x - a - n * d)))
        return
    if x > a + (n - 1) * d:
        print(min(abs(x - a - (n - 1) * d), abs(x - a - n * d)))
        return

if __name__ == '__main__':
    main()