def main():
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    max_a = max(a)
    min_a = min(a)
    max_x = max(x)
    min_x = min(x)
    max_value = max(max_a, max_x)
    min_value = min(min_a, min_x)
    if max_value == min_value:
        print(0)
        return
    a = [ai - min_value for ai in a]
    x = [xi - min_value for xi in x]
    n = max_value - min_value + 1
    d = [0] * n
    for i in range(n - 1):
        d[i + 1] = d[i] + a[i]
    for xi in x:
        if xi == 0:
            print(0)
            continue
        ans = 0
        for i in range(n - 1):
            if d[i] <= xi < d[i + 1]:
                ans += xi * (i + 1) - d[i]
                ans += d[-1] - d[i + 1] - xi * (n - i - 1)
                break
            else:
                ans += d[i + 1] - d[i]
        print(ans)

if __name__ == '__main__':
    main()