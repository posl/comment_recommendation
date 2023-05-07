def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = [sum(p) for p in P]
    P.sort(reverse=True)
    for i in range(N):
        if P[i] < P[K-1]:
            print("No")
        else:
            print("Yes")
