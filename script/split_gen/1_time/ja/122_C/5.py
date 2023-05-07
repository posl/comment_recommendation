def main():
    N, Q = map(int, input().split())
    S = input()
    AC = [0] * (N + 1)
    for i in range(N):
        if S[i] == 'A' and S[i+1] == 'C':
            AC[i+1] = AC[i] + 1
        else:
            AC[i+1] = AC[i]
    for i in range(Q):
        l, r = map(int, input().split())
        print(AC[r-1] - AC[l-1])
