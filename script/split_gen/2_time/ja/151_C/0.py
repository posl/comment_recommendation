def main():
    N, M = map(int, input().split())
    P = []
    S = []
    for i in range(M):
        p, s = input().split()
        P.append(int(p))
        S.append(s)
    AC = [0] * N
    WA = [0] * N
    for i in range(M):
        if S[i] == "AC":
            AC[P[i]-1] += 1
        else:
            WA[P[i]-1] += 1
    wa = 0
    ac = 0
    for i in range(N):
        if AC[i] != 0:
            ac += 1
            wa += WA[i]
    print(ac, wa)
