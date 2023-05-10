def main():
    N, W = map(int, input().split())
    STP = [list(map(int, input().split())) for _ in range(N)]
    STP.sort()
    T = [0] * (2 * 10**5 + 1)
    for s, t, p in STP:
        T[s] += p
        T[t] -= p
    for i in range(2 * 10**5):
        T[i + 1] += T[i]
        if T[i] > W:
            print("No")
            exit()
    print("Yes")
