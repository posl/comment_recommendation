def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if b[i] >= a[i]:
            total += a[i]
            b[i] -= a[i]
            a[i] = 0
        else:
            total += b[i]
            a[i] -= b[i]
            b[i] = 0
        if b[i] >= a[i+1]:
            total += a[i+1]
            b[i] -= a[i+1]
            a[i+1] = 0
        else:
            total += b[i]
            a[i+1] -= b[i]
            b[i] = 0
    print(total)

if __name__ == '__main__':
    main()