def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(a)
    else:
        print(a + k % n if a + k % n <= n else a + k % n - n)

if __name__ == '__main__':
    main()