def main():
    from collections import deque
    N, M = map(int, input().split())
    road = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    for i in range(N):
        road[i].sort()
        road[i] = deque(road[i])
    for i in range(N):
        d = len(road[i])
        print(d, end=" ")
        for _ in range(d):
            print(road[i].popleft()+1, end=" ")
        print()

if __name__ == '__main__':
    main()