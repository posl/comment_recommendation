def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_value = [0] * (n + 1)
    max_value = [0] * (n + 1)
    for i in range(n):
        min_value[a[i]] = i + 1
        max_value[a[i]] = i + 1
    for i in range(1, n + 1):
        min_value[i] = max(min_value[i], min_value[i - 1])
    for i in range(n - 1, 0, -1):
        max_value[i] = min(max_value[i], max_value[i + 1])
    ans = 0
    for i in range(1, n + 1):
        ans += max_value[i] - min_value[i]
    print(ans)

if __name__ == '__main__':
    main()