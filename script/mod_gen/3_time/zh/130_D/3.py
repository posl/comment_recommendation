def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k, a)
    ans = 0
    right = 0
    total = 0
    for left in range(n):
        while right < n and total < k:
            total += a[right]
            right += 1
        if total < k:
            break
        ans += n - right + 1
        if left == right:
            right += 1
        else:
            total -= a[left]
    print(ans)

if __name__ == '__main__':
    main()