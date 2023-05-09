def main():
    N, Q = map(int, input().split())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))
    for _ in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t])
