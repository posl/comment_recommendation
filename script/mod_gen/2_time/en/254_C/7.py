def solve(n, k, a):
    for i in range(n-k):
        if a[i] >= a[i+k]:
            return "Yes"
    return "No"

if __name__ == '__main__':
    solve()