def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0 for _ in range(N)] for _ in range(N)]
    Y = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][x-1] = 1
            Y[i][x-1] = y
    ans = 0
    for i in range(2**N):
        bit = [0 for _ in range(N)]
        for j in range(N):
            if (i >> j) & 1:
                bit[j] = 1
        flag = True
        for j in range(N):
            if bit[j] == 1:
                for k in range(N):
                    if X[j][k] == 1 and bit[k] != Y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, sum(bit))
    print(ans)
