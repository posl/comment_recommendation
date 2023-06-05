def solve(n, a, b):
    # 请在这里编写代码
    sum = 0
    for x in range(a[0], b[0] + 1):
        if all(a[i] <= x <= b[i] for i in range(1, n)):
            sum += 1
    print(sum)

if __name__ == '__main__':
    solve()