def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    X = 0
    Y = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            X += V[i]
            Y += C[i]
    print(X - Y)

if __name__ == '__main__':
    main()