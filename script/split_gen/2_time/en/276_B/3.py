def main():
    N, M = map(int, input().split())
    city = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        city[A].append(B)
        city[B].append(A)
    for i in range(1, N + 1):
        city[i].sort()
        print(len(city[i]), *city[i])
