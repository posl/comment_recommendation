def main():
    N, M = map(int, input().split())
    road = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        road[A-1].append(B-1)
        road[B-1].append(A-1)
    print(road)
