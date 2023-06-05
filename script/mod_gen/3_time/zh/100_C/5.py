def solve(n, a):
    count = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            count += 1
    return count

if __name__ == '__main__':
    solve()