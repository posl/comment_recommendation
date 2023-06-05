def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    ans = 0
    for i in range(N):
        for j in edges[i]:
            if H[i] <= H[j]:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()