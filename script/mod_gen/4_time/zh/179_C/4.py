def solve(n):
    count = 0
    for i in range(1,n):
        if n%i == 0:
            count += 1
    return count

if __name__ == '__main__':
    solve()