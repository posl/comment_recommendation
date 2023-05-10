def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        count = 0
        while k > n:
            k -= n
            count += 1
        if k <= n:
            if k <= a:
                print(k + count * n)
            else:
                print(k + count * n + 1)

if __name__ == '__main__':
    main()