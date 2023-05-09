def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == i+1:
                time += Y[j]
    
    print("Yes")
