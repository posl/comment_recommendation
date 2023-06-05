def main():
    N, X, Y = map(int, input().split())
    X, Y = X-1, Y-1
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)
    # print(tree)
    # print(X, Y)
    # X, Y = 1, 2
    # tree = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 6
    # tree = [[1], [0, 2, 3], [1, 4, 5], [1], [2], [2], [6]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 3
    # tree = [[1], [0, 2, 3], [1, 4, 5], [1], [2], [2], [6]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 6
    # tree = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 5
    # tree = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 4
    # tree = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 1
    # tree = [[1, 2], [0, 3,

if __name__ == '__main__':
    main()