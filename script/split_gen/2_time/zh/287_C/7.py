def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    edges.sort()
    print(edges)
    for i in range(M):
        if edges[i][0] == edges[i+1][0] or edges[i][1] == edges[i+1][1]:
            print("No")
            break
        else:
            print("Yes")
            break
