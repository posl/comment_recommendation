def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    X = 0
    Y = 0
    for i in range(N):
        if V[i] > C[i]:
            X += V[i]
            Y += C[i]
    print(X - Y)
