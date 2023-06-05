def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    right = 0
    for left in range(N):
        while right < N and s + a[right] < K:
            s += a[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            s -= a[left]
    print(ans)

if __name__ == '__main__':
    solve()