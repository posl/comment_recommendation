def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for i in range(n):
        cnt[a[i]] += 1
    sum = 0
    for i in range(1, n + 1):
        sum += cnt[i] * (cnt[i] - 1) // 2
    for i in range(n):
        print(sum - (cnt[a[i]] - 1))

if __name__ == '__main__':
    main()