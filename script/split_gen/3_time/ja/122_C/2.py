def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(N - 1):
        if S[i] == "A" and S[i + 1] == "C":
            l[i + 2] = l[i + 1] + 1
        else:
            l[i + 2] = l[i + 1]
    for _ in range(Q):
        x, y = map(int, input().split())
        print(l[y] - l[x])
