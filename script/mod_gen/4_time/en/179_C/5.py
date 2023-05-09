def solve(n):
    count = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j + i + j > n:
                break
            if (n - i - j) % (i * j) == 0:
                count += 1
    return count

if __name__ == '__main__':
    solve()