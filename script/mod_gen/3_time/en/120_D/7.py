def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.reverse()
    par = [i for i in range(N+1)]
    size = [1 for i in range(N+1)]
    ans = [0 for i in range(M)]
    now = N*(N-1)//2
    for i in range(M):
        a, b = AB[i]
        if find(par, a) != find(par, b):
            now -= size[find(par, a)]*size[find(par, b)]
            unite(par, size, a, b)
        ans[i] = now
    ans.reverse()
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()