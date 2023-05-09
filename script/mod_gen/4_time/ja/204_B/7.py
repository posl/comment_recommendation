def f204_b(n, a):
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    return ans

if __name__ == '__main__':
    f204_b()