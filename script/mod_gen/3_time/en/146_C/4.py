def main():
    a, b, x = map(int, input().split())
    n = x // a
    if n > 10**9:
        n = 10**9
    for i in range(n, 0, -1):
        if a * i + b * len(str(i)) <= x:
            print(i)
            return
    print(0)

if __name__ == '__main__':
    main()