def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(n):
        while right < n and sum < k:
            sum += a[right]
            right += 1
        if sum >= k:
            ans += n - right + 1
        sum -= a[left]
    print(ans)

if __name__ == '__main__':
    main()