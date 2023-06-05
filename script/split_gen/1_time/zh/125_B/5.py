def value_of_gems(N, V, C):
    X = 0
    Y = 0
    for i in range(N):
        if V[i] > C[i]:
            X += V[i]
            Y += C[i]
    return X - Y
N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
print(value_of_gems(N, V, C))
