def solve(n):
    ans = []
    for i in range(1, 1<<15):
        if i & n == i:
            ans.append(i)
    return ans

if __name__ == '__main__':
    solve()