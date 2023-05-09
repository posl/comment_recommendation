def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    xy = []
    for i in range(N):
        xy.append([list(map(int, input().split())) for _ in range(A[i])])
    ans = 0
    for bit in range(1<<N):
        honest = [0 for _ in range(N)]
        for i in range(N):
            if bit & (1<<i):
                honest[i] = 1
        flag = True
        for i in range(N):
            if honest[i] == 1:
                for j in range(A[i]):
                    if honest[xy[i][j][0]-1] != xy[i][j][1]:
                        flag = False
                        break
        if flag:
            ans = max(ans, sum(honest))
    print(ans)
    return

if __name__ == '__main__':
    main()