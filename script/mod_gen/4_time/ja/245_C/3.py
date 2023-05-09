def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    left = 0
    right = 10**9 + 1
    while left < right:
        mid = (left + right) // 2
        is_ok = True
        for i in range(n):
            if a[i] > mid:
                if b[i] >= a[i] - mid:
                    continue
                else:
                    is_ok = False
                    break
            else:
                if b[i] >= a[i] - mid or b[i] <= a[i] + mid:
                    continue
                else:
                    is_ok = False
                    break
        if is_ok:
            right = mid
        else:
            left = mid + 1
    print("Yes" if left <= k else "No")

if __name__ == '__main__':
    main()