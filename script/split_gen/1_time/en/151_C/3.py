def main():
    N, M = map(int, input().split())
    ac = [0] * N
    wa = [0] * N
    for _ in range(M):
        p, S = input().split()
        p = int(p) - 1
        if ac[p] == 0:
            if S == "AC":
                ac[p] = 1
            else:
                wa[p] += 1
    ac_sum = sum(ac)
    wa_sum = sum([wa[i] for i in range(N) if ac[i] == 1])
    print(ac_sum, wa_sum)
