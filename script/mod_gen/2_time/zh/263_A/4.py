def func(n, a):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if sum(a[i:j + 1]) % len(a[i:j + 1]) == 0:
                ans += 1
    return ans

if __name__ == '__main__':
    func()