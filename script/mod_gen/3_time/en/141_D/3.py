def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    i = 0
    while i < m and a[i] >= a[0] / (2 ** (i + 1)):
        i += 1
    print(sum(a[i:]) + a[0] * (2 ** (i + 1) - 1))

if __name__ == '__main__':
    main()