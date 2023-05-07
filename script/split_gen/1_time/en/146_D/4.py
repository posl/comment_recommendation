def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(i)
        G[b-1].append(i)
    K = 0
    for i in range(N):
        K = max(K, len(G[i]))
    print(K)
    for i in range(N):
        for j in range(len(G[i])):
            print(j+1)
