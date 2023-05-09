def main():
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    X = 0
    Y = 0
    for i in range(N):
        if V[i]-C[i] > 0:
            X += V[i]
            Y += C[i]
    print(X-Y)
