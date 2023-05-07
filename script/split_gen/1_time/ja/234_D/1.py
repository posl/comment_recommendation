def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p-1 for p in P]
    C = [0] * N
    for p in P:
        C[p] += 1
    S = 0
    for i in range(N):
        S += C[i]
        if S >= K:
            print(i+1)
            break
