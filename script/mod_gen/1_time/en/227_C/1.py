def solve(n):
    count = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            for c in range(b, n+1):
                if a*b*c <= n:
                    count += 1
                else:
                    break
    return count

if __name__ == '__main__':
    solve()