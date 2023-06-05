def solve(N, V):
    V.sort()
    for i in range(N - 1):
        V[i + 1] = (V[i] + V[i + 1]) / 2
    return V[-1]
