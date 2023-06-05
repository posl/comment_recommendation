def pizza_cut(n, a):
    """切割比萨饼"""
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            ans = max(ans, abs(a[i] - a[j]))
            ans = max(ans, 360 - abs(a[i] - a[j]))
    return ans

if __name__ == '__main__':
    pizza_cut()