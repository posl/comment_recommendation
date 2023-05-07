def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        if sum(P[i]) + (3 * (K - 1)) >= sum(P[K - 1]):
            print("Yes")
        else:
            print("No")
