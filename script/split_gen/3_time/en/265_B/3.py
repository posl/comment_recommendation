def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    X.append(N)
    Y.append(0)
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        j = 0
        while j < M+1 and X[j] < i+2:
            j += 1
        if j < M+1 and X[j] == i+2:
            t += Y[j]
    print("Yes")
    return
