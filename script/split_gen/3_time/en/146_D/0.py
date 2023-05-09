def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    c = [0] * (N-1)
    color = 1
    for i in range(N):
        for j in G[i]:
            if c[j] == 0:
                c[j] = color
                color += 1
    print(max(c))
    for i in range(N-1):
        print(c[i])
