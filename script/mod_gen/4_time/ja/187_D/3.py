def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if n % 2 == 0:
        a_med = (a[n // 2 - 1] + a[n // 2]) // 2
        b_med = (b[n // 2 - 1] + b[n // 2]) // 2
    else:
        a_med = a[n // 2]
        b_med = b[n // 2]
    print(b_med - a_med + 1)

if __name__ == '__main__':
    main()