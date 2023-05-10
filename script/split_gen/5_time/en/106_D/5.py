def main():
    N, M, Q = map(int, input().split())
    trains = []
    for i in range(M):
        trains.append(list(map(int, input().split())))
    trains.sort(key=lambda x: x[0])
    for i in range(Q):
        p, q = map(int, input().split())
        count = 0
        for j in range(M):
            if trains[j][0] < p:
                continue
            if trains[j][1] > q:
                break
            count += 1
        print(count)
