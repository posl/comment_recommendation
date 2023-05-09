def main():
    a, b, k = map(int, input().split())
    if a + b <= k:
        print(0, 0)
    elif a <= k:
        print(0, b - (k - a))
    else:
        print(a - k, b)

if __name__ == '__main__':
    main()