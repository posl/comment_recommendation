def solve():
    n = int(input())
    ans = []
    for i in range(0, 61):
        if n & (1 << i) != 0:
            ans.append(i)
    for i in range(0, len(ans)):
        print(1 << ans[i])

if __name__ == '__main__':
    solve()