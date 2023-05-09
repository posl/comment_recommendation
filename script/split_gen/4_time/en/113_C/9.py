def main():
    N, M = map(int, input().split())
    PY = [[int(x) for x in input().split()] for _ in range(M)]
    PY = sorted(PY, key=lambda x: x[1])
    P = [0] * N
    for i in range(M):
        P[PY[i][0] - 1] += 1
        PY[i].append(P[PY[i][0] - 1])
    PY = sorted(PY, key=lambda x: x[2])
    for i in range(M):
        print(str(PY[i][0]).zfill(6) + str(PY[i][3]).zfill(6))
