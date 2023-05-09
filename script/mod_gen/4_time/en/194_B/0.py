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
        a_m = (a[n // 2] + a[n // 2 - 1]) // 2
        b_m = (b[n // 2] + b[n // 2 - 1]) // 2
        print(b_m - a_m + 1)
    else:
        a_m = a[n // 2]
        b_m = b[n // 2]
        print(b_m - a_m + 1)

if __name__ == '__main__':
    main()