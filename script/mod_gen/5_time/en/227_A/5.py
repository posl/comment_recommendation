def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        k -= n
        print(n - k % n if k % n != 0 else n)

if __name__ == '__main__':
    main()