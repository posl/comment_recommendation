def solve(n, k, a):
    a = a[::-1]
    count = 0
    for i in range(n):
        if a[i] == i + 1:
            count += 1
            i += k - 1
    return (n + k - 1) // k - (count + k - 1) // k

if __name__ == '__main__':
    solve()