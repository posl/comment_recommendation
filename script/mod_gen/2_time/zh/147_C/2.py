def is_honest(i, N, A, xy):
    for j in range(A[i]):
        if xy[i][j][1] == 1:
            if xy[i][j][0] not in honest:
                honest.append(xy[i][j][0])
                is_honest(xy[i][j][0] - 1, N, A, xy)
        else:
            if xy[i][j][0] in honest:
                return False
    return True
N = int(input())
A = []
xy = []
for i in range(N):
    A.append(int(input()))
    xy.append([])
    for j in range(A[i]):
        xy[i].append(list(map(int, input().split())))
max_honest = 0
for i in range(N):
    honest = []
    if is_honest(i, N, A, xy):
        max_honest = max(max_honest, len(honest))
print(max_honest)

if __name__ == '__main__':
    is_honest()