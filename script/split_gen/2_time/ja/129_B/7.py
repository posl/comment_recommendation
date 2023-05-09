def main():
    N = int(input())
    W = list(map(int, input().split()))
    T = 1
    S1 = 0
    S2 = 0
    while T < N:
        for i in range(T):
            S1 += W[i]
        for j in range(T, N):
            S2 += W[j]
        T += 1
        print(abs(S1 - S2))
