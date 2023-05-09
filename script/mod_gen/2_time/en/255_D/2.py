def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        ans = 0
        left = 0
        right = n - 1
        while left < right:
            if a[left] < x[i]:
                left += 1
            if a[right] > x[i]:
                right -= 1
            if a[left] >= x[i] and a[right] <= x[i]:
                break
        ans += min(abs(a[left] - x[i]), abs(a[right] - x[i]))
        ans += abs(a[left] - a[right])
        print(ans)

if __name__ == '__main__':
    main()