def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    right = 0
    s = 0
    for left in range(n):
        while right < n and s + a[right] < k:
            s += a[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            s -= a[left]
    print(ans)
