def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    if M != N - 1:
        print("No")
        return
    for i in range(M):
        for j in range(i + 1, M):
            if edges[i][0] == edges[j][0] or edges[i][0] == edges[j][1] or edges[i][1] == edges[j][0] or edges[i][1] == edges[j][1]:
                print("No")
                return
    print("Yes")
