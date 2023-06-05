def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(0)
    # 从a[0]开始，逆时针方向的最大值
    left = [0] * (n + 2)
    # 从a[n-1]开始，顺时针方向的最大值
    right = [0] * (n + 2)
    for i in range(n):
        left[i + 1] = max(left[i], a[i])
        right[n - i] = max(right[n - i + 1], a[n - i - 1])
    ans = 0
    for i in range(n):
        ans = max(ans, a[i] + min(left[i], right[i + 2]))
    print(ans)
