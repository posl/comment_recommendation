def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    edges.sort()
    #print(edges)
    if edges[0][0] != 1:
        print('No')
        exit()
    for i in range(n-1):
        if edges[i][0] != edges[i+1][0]:
            print('No')
            exit()
    print('Yes')
