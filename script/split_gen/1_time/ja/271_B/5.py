def main():
    N, Q = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    S, T = zip(*[map(int, input().split()) for _ in range(Q)])
    for s, t in zip(S, T):
        print(L[s-1][t])
