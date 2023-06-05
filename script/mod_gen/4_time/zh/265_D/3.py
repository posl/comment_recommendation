def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    # 从左到右计算A_{x}+A_{x+1}+...+A_{y-1}的最大值
    max_a = [0] * n
    max_a[0] = a[0]
    for i in range(1, n):
        max_a[i] = max(max_a[i - 1], a[i])
    # 从右到左计算A_{z}+A_{z+1}+...+A_{w-1}的最大值
    max_c = [0] * n
    max_c[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        max_c[i] = max(max_c[i + 1], a[i])
    # 计算A_{y}+A_{y+1}+...+A_{z-1}的最大值
    s = [0] * n
    s[0] = a[0]
    for i in range(1, n):
        s[i] = s[i - 1] + a[i]
    # 计算结果
    ans = 'No'
    for i in range(1, n - 1):
        if p <= a[i] <= q and max_a[i - 1] >= p and max_c[i + 1] >= r and s[i - 1] >= p * (i - 1) and s[n - 1] - s[i] >= r * (n - i - 1):
            ans = 'Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()