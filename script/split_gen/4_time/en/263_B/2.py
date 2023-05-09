def main():
    N = int(input())
    P = list(map(int, input().split()))
    G = [0] * N
    for i in range(N):
        if P[i] == 1:
            G[i] = 1
        else:
            G[i] = G[P[i]-1] + 1
    print(max(G))
