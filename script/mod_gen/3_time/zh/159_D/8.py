def main():
    n = int(input())
    a = list(map(int, input().split()))
    num = {}
    for i in range(n):
        if a[i] not in num:
            num[a[i]] = 1
        else:
            num[a[i]] += 1
    total = 0
    for i in num:
        total += num[i] * (num[i] - 1) // 2
    for i in range(n):
        print(total - num[a[i]] + 1)

if __name__ == '__main__':
    main()