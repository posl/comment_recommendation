def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges = sorted(edges, key=lambda x: x[0])
    # print(edges)
    flag = True
    for i in range(len(edges)-1):
        if edges[i][1] != edges[i+1][0]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")
