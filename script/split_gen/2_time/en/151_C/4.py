def main():
    N, M = map(int, input().split())
    S = [0] * N
    P = [0] * N
    for i in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            S[p - 1] = 1
        else:
            if S[p - 1] == 0:
                P[p - 1] += 1
    ans1 = 0
    ans2 = 0
    for i in range(N):
        if S[i] == 1:
            ans1 += 1
            ans2 += P[i]
    print(ans1, ans2)
