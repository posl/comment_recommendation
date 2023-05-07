def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        for j in range(i+1, N):
            if T[i][j] != T[j][i]:
                print("T[i][j] != T[j][i]")
                return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if T[i][j] > K:
                print("T[i][j] > K")
                return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if T[i][j] + T[j][i] > K:
                print("T[i][j] + T[j][i] > K")
                return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if T[i][j] + T[j][i] + T[i][j] > K:
                print("T[i][j] + T[j][i] + T[i][j] > K")
                return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if T[i][j] + T[j][i] + T[i][j] + T[j][i] > K:
                print("T[i][j] + T[j][i] + T[i][j] + T[j][i] > K")
                return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if T[i][j] + T[j][i] + T[i][j] + T[j][i] + T[i][j] > K:
                print("T[i][j] + T[j][i] + T[i][j] + T[j][i] + T[i][j] > K")
                return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if T[i][j] + T[j][i] + T[i][j] + T[j][i] + T[i][j] + T

if __name__ == '__main__':
    main()