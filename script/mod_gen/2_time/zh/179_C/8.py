def solve(n):
    count = 0
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            count += 1
            if i * i < n:
                count += 1
    return count

if __name__ == '__main__':
    solve()