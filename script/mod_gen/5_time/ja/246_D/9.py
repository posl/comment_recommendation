def solve(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 9
    else:
        return solve(n-1)+solve(n-2)+solve(n-3)+solve(n-4)
n = int(input())
print(solve(n))

if __name__ == '__main__':
    solve()