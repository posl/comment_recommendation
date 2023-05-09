def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    if M == 0:
        print("Yes")
        return
    for i in range(N):
        if len(G[i]) == 0:
            print("No")
            return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if len(set(G[i]) & set(G[j])) == 0:
                print("No")
                return
    print("Yes")
main()
