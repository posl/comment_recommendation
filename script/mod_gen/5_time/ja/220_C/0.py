def func(n, a, x):
    b = a * (x // sum(a))
    ans = n * (x // sum(b))
    x -= sum(b) * (x // sum(b))
    for i in range(n):
        x -= b[i]
        ans += 1
        if x < 0:
            break
    return ans

if __name__ == '__main__':
    func()