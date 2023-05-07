def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print('No')
        return
    parent = list(range(n))
    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]
    def union(i, j):
        parent[find(i)] = find(j)
    for _ in range(m):
        i, j = map(int, input().split())
        union(i - 1, j - 1)
    print('Yes' if len(set(find(i) for i in range(n))) == 1 else 'No')

if __name__ == '__main__':
    main()