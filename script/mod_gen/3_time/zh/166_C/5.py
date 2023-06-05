def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    edges = []
    for i in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    ans = 0
    for i in range(n):
        flag = True
        for edge in edges:
            if i+1 in edge:
                if h[i] <= h[edge[0]-1] or h[i] <= h[edge[1]-1]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()