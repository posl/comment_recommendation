def main():
    N, M = map(int, input().split())
    bridge = [tuple(map(int, input().split())) for i in range(M)]
    bridge.reverse()
    #print(bridge)
    ans = [0]*M
    ans[0] = N*(N-1)//2
    parent = [i for i in range(N+1)]
    size = [1]*(N+1)
    for i in range(1, M):
        a, b = bridge[i-1]
        if parent[a] == parent[b]:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] - size[parent[a]]*size[parent[b]]
            if size[parent[a]] > size[parent[b]]:
                a, b = b, a
            size[parent[b]] += size[parent[a]]
            parent[a] = parent[b]
    ans.reverse()
    for i in range(M):
        print(ans[i])
main()
