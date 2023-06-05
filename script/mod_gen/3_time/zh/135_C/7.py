def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if b[i] >= a[i]:
            total += a[i]
            b[i] -= a[i]
            if b[i] >= a[i+1]:
                total += a[i+1]
                b[i] -= a[i+1]
            else:
                total += b[i]
                b[i+1] -= b[i]
        else:
            total += b[i]
    print(total)

if __name__ == '__main__':
    main()