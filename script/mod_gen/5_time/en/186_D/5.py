def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        sum += a[i] * (n - i - 1) - a[i] * i
    print(sum)

if __name__ == '__main__':
    main()