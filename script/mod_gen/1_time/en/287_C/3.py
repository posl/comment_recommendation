def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort()
    for i in range(M):
        if edges[i][0] != i + 1 or edges[i][1] != i + 2:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()