def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        sum += a[i] * (2 * i - n + 1)
    print(sum)

if __name__ == '__main__':
    main()