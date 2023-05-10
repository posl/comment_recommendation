def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] >= 0:
        return sum(a) - 2 * a[0]
    elif a[-1] <= 0:
        return 2 * abs(a[-1]) - sum(a)
    else:
        return sum(map(abs, a))
print(solve())

if __name__ == '__main__':
    solve()