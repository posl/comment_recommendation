def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = [0] * (n + 1)
    for i in range(n):
        sum_a[i + 1] = sum_a[i] + a[i]
    ans = 0
    right = 0
    for left in range(n):
        while right < n + 1 and sum_a[right] - sum_a[left] < k:
            right += 1
        ans += n + 1 - right
    print(ans)

if __name__ == '__main__':
    main()