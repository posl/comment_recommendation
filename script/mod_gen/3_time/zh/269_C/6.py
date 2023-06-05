def solve(n):
    ans = []
    for i in range(1, 2**15):
        x = 0
        for j in range(15):
            if i & (1 << j):
                x |= 1 << (j * (i & (1 << j)))
        if x <= n:
            ans.append(x)
    return ans

if __name__ == '__main__':
    solve()