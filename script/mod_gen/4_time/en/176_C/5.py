def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    sum = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            sum += a[i] - a[i-1]
            a[i] = a[i-1]
    print(sum)

if __name__ == '__main__':
    main()