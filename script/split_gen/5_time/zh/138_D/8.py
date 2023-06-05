def main():
    n, q = map(int, input().split())
    links = []
    for _ in range(n - 1):
        links.append(list(map(int, input().split())))
    operations = []
    for _ in range(q):
        operations.append(list(map(int, input().split())))
    tree = []
    for _ in range(n):
        tree.append(0)
    for operation in operations:
        tree[operation[0] - 1] += operation[1]
    for link in links:
        if link[0] == 1:
            tree[link[1] - 1] += tree[0]
        else:
            tree[link[1] - 1] += tree[link[0] - 1]
    print(' '.join(map(str, tree)))
