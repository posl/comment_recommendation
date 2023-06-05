def main():
    N, M = map(int, input().split())
    PY = [list(map(int, input().split())) for i in range(M)]
    PY = sorted(PY, key=lambda x: x[1])
    # print(PY)
    # print(N, M)
    # print(PY)
    city = [0] * N
    for i in range(M):
        city[PY[i][0] - 1] += 1
        PY[i].append(city[PY[i][0] - 1])
    # print(PY)
    for i in range(M):
        print(str(PY[i][0]).zfill(6) + str(PY[i][3]).zfill(6))
