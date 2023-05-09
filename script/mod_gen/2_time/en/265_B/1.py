def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    ans = 'Yes'
    time = 0
    max_time = T
    for i in range(N):
        if i == 0:
            time += A[i]
        elif i == N-1:
            time += A[i]
        else:
            time += A[i] - A[i-1]
        for j in range(M):
            if i == X[j]-1:
                time += Y[j]
        if time > max_time:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()