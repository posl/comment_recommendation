def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    C = [0]*N
    for i in range(N):
        C[i] = [0]*(len(G[i])+1)
    for i in range(N):
        for j in range(len(G[i])):
            C[i][j+1] = C[i][j] + 1
    for i in range(N):
        for j in range(len(G[i])):
            for k in range(j+1, len(G[i])):
                if C[G[i][j]][i+1] == C[G[i][k]][i+1]:
                    C[G[i][k]][i+1] += 1
    print(max(C[i]) + 1)
    for i in range(N):
        for j in range(len(G[i])):
            if i < G[i][j]:
                print(C[i][j+1])

if __name__ == '__main__':
    main()