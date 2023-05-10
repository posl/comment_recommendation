def main():
    N, Q = map(int, input().split())
    S = input()
    AC_count = [0] * (N + 1)
    for i in range(1, N):
        AC_count[i + 1] = AC_count[i]
        if S[i - 1] == 'A' and S[i] == 'C':
            AC_count[i + 1] += 1
    for _ in range(Q):
        l, r = map(int, input().split())
        print(AC_count[r] - AC_count[l])
