def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        left = 0
        while left < n and h[left] == 0:
            left += 1
        if left == n:
            break
        right = left
        while right < n and h[right] != 0:
            right += 1
        min_h = min(h[left:right])
        for i in range(left, right):
            h[i] -= min_h
        ans += min_h
    print(ans)
