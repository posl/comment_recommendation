def main():
    N, M = map(int, input().split())
    roads = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        roads[a] += 1
        roads[b] += 1
    for i in range(1, N + 1):
        print(roads[i], end = " ")
        for j in range(1, N + 1):
            if i != j and roads[j] >= 1:
                print(j, end = " ")
        print()
