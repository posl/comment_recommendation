def solve(n, a, b):
    ans = []
    for i in range(n):
        if i < n//2:
            ans.append("."*b + "#"*b)
        else:
            ans.append("#"*b + "."*b)
    return ans

if __name__ == '__main__':
    solve()