def main():
    n, k, a = map(int, input().split())
    k = k % n
    if a + k <= n:
        print(a + k)
    else:
        print(a + k - n)

if __name__ == '__main__':
    main()