def problems129_b():
    N = int(input())
    W = [int(i) for i in input().split()]
    min_diff = sum(W)
    for i in range(N):
        S1 = sum(W[0:i+1])
        S2 = sum(W[i+1:N])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
