def main():
    N, Q = map(int, input().split())
    parent = [i for i in range(N+1)]
    size = [1 for i in range(N+1)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            y = query[2]
            parent[x] = y
            size[y] += size[x]
        elif query[0] == 2:
            x = query[1]
            y = query[2]
            parent[x] = x
            size[y] -= size[x]
        else:
            x = query[1]
            print(size[x], end=' ')
            for j in range(1, N+1):
                if parent[j] == x:
                    print(j, end=' ')
            print()
main()

if __name__ == '__main__':
    main()