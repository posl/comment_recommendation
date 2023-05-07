def main():
    N, M = map(int, input().split())
    path = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        path[a-1].add(b-1)
        path[b-1].add(a-1)
    for i in range(N):
        print(len(path[i]), *sorted(path[i])+1)
