def solve():
    # ++++ INPUT ++++
    S = input()
    N = len(S)
    # ++++ SOLVE ++++
    ans = [0] * N
    # R の位置を記録
    R = []
    for i in range(N):
        if S[i] == 'R':
            R.append(i)
    # R の位置を元に、各マスの人数を計算
    for i in range(N):
        # R の位置より左にある L の数
        # R の位置より右にある R の数
        # R の位置より右にある L の数
        # R の位置より左にある R の数
        r1 = len([r for r in R if r < i])
        r2 = len([r for r in R if r > i])
        l1 = i - r1
        l2 = N - i - r2
        # L から R に移動する人数
        if S[i] == 'L':
            ans[i - 1] += l1
            ans[i] += l2
        # R から L に移動する人数
        else:
            ans[i] += r1
            ans[i - 1] += r2
    # ++++ OUTPUT ++++
    print(*ans)

if __name__ == '__main__':
    solve()