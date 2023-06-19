def solve(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 1:
            count += 1
    return count

if __name__ == '__main__':
    solve()