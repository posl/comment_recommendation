def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x: x[0])
    if edges[0][0] == 1:
        for i in range(M-1):
            if edges[i][1] != edges[i+1][0]:
                print("No")
                exit()
        print("Yes")
    elif edges[-1][1] == N:
        for i in range(M-1):
            if edges[i][1] != edges[i+1][0]:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()