def main():
    N, W = map(int, input().split())
    T = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        s, t, p = map(int, input().split())
        T[s] += p
        T[t] -= p
    for i in range(1, 2 * 10 ** 5 + 1):
        T[i] += T[i - 1]
        if T[i] > W:
            print("No")
            exit()
    print("Yes")
