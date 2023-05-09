def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    left = 0
    right = n - 1
    while left < right:
        if a[left] + a[right] < k:
            left += 1
        else:
            ans += right - left
            right -= 1
    print(ans)

if __name__ == '__main__':
    main()