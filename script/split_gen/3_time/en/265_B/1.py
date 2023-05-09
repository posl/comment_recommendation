def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    ans = "Yes"
    t = T
    for i in range(N-1):
        t = t - A[i]
        if t <= 0:
            ans = "No"
            break
        for j in range(M):
            if X[j] == i+1:
                t = t + Y[j]
                if t > T:
                    t = T
    print(ans)
