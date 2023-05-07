def main():
    N, Q = map(int, input().split())
    S = input()
    AC = [0] * (N + 1)
    for i in range(1, N):
        if S[i - 1] == 'A' and S[i] == 'C':
            AC[i + 1] = AC[i] + 1
        else:
            AC[i + 1] = AC[i]
    for i in range(Q):
        l, r = map(int, input().split())
        print(AC[r] - AC[l])
