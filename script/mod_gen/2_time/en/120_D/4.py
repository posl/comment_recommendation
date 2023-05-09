def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.reverse()
    ans = [0] * M
    ans[0] = (N - 1) * N // 2
    parent = list(range(N + 1))
    size = [1] * (N + 1)
    for i in range(M - 1):
        a, b = bridges[i]
        pa = root(a, parent)
        pb = root(b, parent)
        if pa != pb:
            ans[i + 1] = ans[i] - (size[pa] * size[pb])
            union(pa, pb, parent, size)
        else:
            ans[i + 1] = ans[i]
    ans.reverse()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()