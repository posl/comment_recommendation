def main():
    N, Q = map(int, input().split())
    cars = [i for i in range(N + 1)]
    root = cars.copy()
    size = [1 for i in range(N + 1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1], query[2]
            root[y] = x
            size[x] += size[y]
        elif query[0] == 2:
            x, y = query[1], query[2]
            root[y] = y
            size[x] -= size[y]
        else:
            x = query[1]
            print(size[x], end=' ')
            for i in range(1, N + 1):
                if root[i] == x:
                    print(i, end=' ')
            print()
