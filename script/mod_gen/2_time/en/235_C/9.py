def main():
    # Get input
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    queries = []
    for _ in range(q):
        queries.append([int(x) for x in input().split()])
    # Process queries
    counts = {}
    for i in range(n):
        if a[i] in counts:
            counts[a[i]].append(i)
        else:
            counts[a[i]] = [i]
    # Output
    for x, k in queries:
        if x not in counts:
            print(-1)
        elif len(counts[x]) < k:
            print(-1)
        else:
            print(counts[x][k-1]+1)

if __name__ == '__main__':
    main()