def solve(N, a):
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    return count

if __name__ == '__main__':
    solve()