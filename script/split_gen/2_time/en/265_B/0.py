def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    for i in range(N-1):
        T = T - A[i]
        if T <= 0:
            print("No")
            break
        else:
            if i+1 in X:
                T = T + Y[X.index(i+1)]
                if T >= 10**9:
                    T = 10**9
            if i == N-2:
                print("Yes")
    else:
        print("Yes")
