def solve(N, K, xs):
    #print(N,K,xs)
    if K == 1:
        return 0
    if K == N:
        return xs[-1] - xs[0]
    if K == 2:
        return min(xs[-1] - xs[0], xs[-2] - xs[0], xs[-1] - xs[1])
    if K == N - 1:
        return min(xs[-1] - xs[0], xs[-1] - xs[1], xs[-2] - xs[0])
    return min(xs[-1] - xs[0] + min(xs[-1] - xs[1], xs[-2] - xs[0]), xs[-2] - xs[0] + xs[-1] - xs[1], xs[-1] - xs[0] + xs[-1] - xs[2])
