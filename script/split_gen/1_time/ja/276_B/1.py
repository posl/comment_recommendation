def main():
    N, M = map(int, input().split())
    road = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        road[A-1].append(B)
        road[B-1].append(A)
    for i in range(N):
        road[i].sort()
        print(len(road[i]), end = ' ')
        print(*road[i])
