def main():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    points = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        points[p-1] += x
    queue = [0]
    while queue:
        p = queue.pop()
        for i in tree[p]:
            if points[i] == 0:
                points[i] = points[p]
                queue.append(i)
    print(*points)

if __name__ == '__main__':
    main()