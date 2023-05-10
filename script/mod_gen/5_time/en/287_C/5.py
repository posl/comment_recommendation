def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x: x[0])
    if edges[0][0] != 1 or edges[-1][1] != n:
        print("No")
        return
    for i in range(1, m):
        if edges[i][0] != edges[i-1][1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()