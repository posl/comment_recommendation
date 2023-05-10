def solve():
    L = int(input())
    ans = 1
    for i in range(1, 12):
        ans *= (L - i)
        ans //= i + 1
    print(ans)
solve()

if __name__ == '__main__':
    solve()