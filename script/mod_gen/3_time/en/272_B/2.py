def main():
    n, m = map(int, input().split())
    d = [0] * n
    for _ in range(m):
        k, *x = map(int, input().split())
        for i in range(k):
            d[x[i] - 1] += 1
    print('Yes' if all(x > 0 for x in d) else 'No')

if __name__ == '__main__':
    main()