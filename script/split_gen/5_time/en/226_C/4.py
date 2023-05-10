def main():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        t = []
        k, *a = map(int, input().split())
        T.append(k)
        K.append(k)
        A.append(a)
    for i in range(N):
        if K[i] == 0:
            T[i] = 0
            continue
        for j in range(K[i]):
            T[i] += T[A[i][j]-1]
    print(max(T))
