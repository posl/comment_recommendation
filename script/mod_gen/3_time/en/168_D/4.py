def main():
    N, M = map(int, input().split())
    G = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)
    ans = [-1]*N
    ans[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for i in G[v]:
            if ans[i] == -1:
                ans[i] = v
                q.append(i)
    print("Yes")
    for i in range(1, N):
        print(ans[i]+1)
main()

if __name__ == '__main__':
    main()