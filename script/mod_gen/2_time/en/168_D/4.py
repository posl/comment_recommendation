def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    if N == 2:
        print('Yes')
        print(1)
        return
    if any(len(adj[i]) == 1 for i in range(1, N)):
        print('No')
        return
    print('Yes')
    for i in range(1, N):
        for j in adj[i]:
            if j != 0 and len(adj[j]) > 1:
                print(j+1)
                break

if __name__ == '__main__':
    main()