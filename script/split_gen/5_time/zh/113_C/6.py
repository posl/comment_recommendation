def getID(p, y):
    return str(p).zfill(6) + str(y).zfill(6)
N, M = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(M)]
PY.sort(key=lambda x: (x[0], x[1]))
ans = [getID(PY[0][0], 1)]
for i in range(1, M):
    if PY[i][0] == PY[i-1][0]:
        ans.append(getID(PY[i][0], len(ans)+1))
    else:
        ans.append(getID(PY[i][0], 1))
for i in ans:
    print(i)
