def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    time = T
    room = 1
    for i in range(N - 1):
        time += Y[i] - (X[i] - room)
        if time <= 0:
            print("No")
            return
        room = X[i]
        time -= A[i]
        if time <= 0:
            print("No")
            return
    
    time += Y[N - 1] - (N - room)
    if time <= 0:
        print("No")
        return
    print("Yes")
    return
