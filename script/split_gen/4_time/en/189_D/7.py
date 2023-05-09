def main():
    N = int(input())
    S = [input() for _ in range(N)]
    Y = [0] * (N+1)
    Y[0] = 1
    for i in range(N):
        if S[i] == 'AND':
            Y[i+1] = Y[i]
        else:
            Y[i+1] = 2**i + Y[i]
    print(Y[N])
main()
