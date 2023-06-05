def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(10):
        for j in range(n):
            if s[j][i] == str((i+1)%10):
                ans = max(ans, j+1)
    print(ans)

if __name__ == '__main__':
    solve()