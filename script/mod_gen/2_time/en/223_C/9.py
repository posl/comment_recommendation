def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    left = 0
    right = 0
    for a, b in AB:
        left += a / b
        right += a / b
    right -= AB[-1][0] / AB[-1][1]
    while right - left > 0.0000000001:
        mid = (right + left) / 2
        left_sum = 0
        for a, b in AB:
            left_sum += max(0, a - mid * b) / b
        if left_sum > mid:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    solve()