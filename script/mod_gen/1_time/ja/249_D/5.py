def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and k != i and a[i] / a[j] == a[k]:
                    ans += 1
    return ans

if __name__ == '__main__':
    solve()