def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0, 0)
        return
    ac = [0] * (N + 1)
    wa = [0] * (N + 1)
    for _ in range(M):
        p, S = input().split()
        p = int(p)
        if ac[p] == 0:
            if S == 'AC':
                ac[p] = 1
            else:
                wa[p] += 1
    AC = 0
    WA = 0
    for i in range(1, N + 1):
        if ac[i] == 1:
            AC += 1
            WA += wa[i]
    print(AC, WA)
