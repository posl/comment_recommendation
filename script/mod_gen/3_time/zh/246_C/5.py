def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        if k > 0:
            if a[i] < x:
                sum += a[i]
                k -= 1
            else:
                sum += x
        else:
            sum += a[i]
    print(sum)

if __name__ == '__main__':
    main()