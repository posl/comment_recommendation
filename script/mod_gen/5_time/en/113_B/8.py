def problem113_b():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    t -= a
    ans = 0
    min_diff = 1e9
    for i in range(n):
        diff = abs(t - h[i] * 0.006)
        if diff < min_diff:
            ans = i + 1
            min_diff = diff
    print(ans)

if __name__ == '__main__':
    problem113_b()