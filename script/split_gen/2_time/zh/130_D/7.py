def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(n):
        while right < n and total + a[right] < k:
            total += a[right]
            right += 1
        ans += right - left
        if left == right:
            right += 1
        else:
            total -= a[left]
    print(ans)
