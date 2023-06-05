def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    # print(edges)
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            u, v, w = edges[i]
            if u < v:
                ans += w
    print(ans)

if __name__ == '__main__':
    main()