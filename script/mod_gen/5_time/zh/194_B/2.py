def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if n % 2 == 0:
        a_median = (a[n // 2] + a[n // 2 - 1]) / 2
        b_median = (b[n // 2] + b[n // 2 - 1]) / 2
        print(int(b_median - a_median + 1))
    else:
        a_median = a[n // 2]
        b_median = b[n // 2]
        print(int(b_median - a_median + 1))

if __name__ == '__main__':
    main()