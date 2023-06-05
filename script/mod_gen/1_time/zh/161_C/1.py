def solve(n,k):
    ans = n
    while True:
        if ans > abs(ans-k):
            ans = abs(ans-k)
        else:
            break
    return ans

if __name__ == '__main__':
    solve()