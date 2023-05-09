def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort(key=lambda x: x[0])
    edges.sort(key=lambda x: x[1])
    print(edges)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (i+1, j+1) not in edges:
                print(i+1, j+1)
                count += 1
    print(count)
