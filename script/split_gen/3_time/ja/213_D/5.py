def main():
    N = int(input())
    road = [[] for _ in range(N)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        road[A-1].append(B-1)
        road[B-1].append(A-1)
    print(*road)
