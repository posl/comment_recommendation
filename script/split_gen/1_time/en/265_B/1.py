def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    time = 0
    for i in range(N-1):
        time += A[i]
        for j in range(M):
            if i+1 == X[j]:
                time += Y[j]
                break
        if time > T:
            print("No")
            return
    print("Yes")
