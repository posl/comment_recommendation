def main():
    n, m = list(map(int, input().strip().split()))
    road = [[] for i in range(n)]
    for i in range(m):
        a, b = list(map(int, input().strip().split()))
        road[a-1].append(b)
        road[b-1].append(a)
    for i in range(n):
        print(len(road[i]), end=" ")
        print(*sorted(road[i]))
