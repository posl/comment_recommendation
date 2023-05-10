def solve(n,m,as_):
    if m == 0:
        return 1
    if n == m:
        return 0
    as_.sort()
    diffs = []
    for i in range(m-1):
        diff = as_[i+1] - as_[i] - 1
        if diff > 0:
            diffs.append(diff)
    diff = as_[0] - 1
    if diff > 0:
        diffs.append(diff)
    diff = n - as_[-1]
    if diff > 0:
        diffs.append(diff)
    diffs.sort()
    k = diffs[0]
    ans = 0
    for diff in diffs:
        ans += (diff + k - 1) // k
    return ans
n,m = map(int, input().split())
as_ = list(map(int, input().split()))
print(solve(n,m,as_))

if __name__ == '__main__':
    solve()