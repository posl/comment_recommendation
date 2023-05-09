def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    p_ac = [0] * (N + 1)
    p_wa = [0] * (N + 1)
    for i in range(M):
        p[i], S[i] = input().split()
        p[i] = int(p[i])
        if S[i] == "AC":
            p_ac[p[i]] = 1
        else:
            if p_ac[p[i]] == 1:
                continue
            else:
                p_wa[p[i]] += 1
    ac = 0
    wa = 0
    for i in range(1, N + 1):
        if p_ac[i] == 1:
            ac += 1
            wa += p_wa[i]
    print(ac, wa)
