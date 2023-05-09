def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # coloring
    C = [0]*N
    for i in range(N):
        C[i] = len(set(C[j] for j in G[i])) + 1
    # output
    print(max(C))
    for i in range(N-1):
        print(C[i])
main()

if __name__ == '__main__':
    main()