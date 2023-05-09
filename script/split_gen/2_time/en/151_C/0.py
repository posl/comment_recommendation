def main():
    N, M = map(int, input().split())
    AC = [0] * (N + 1)
    WA = [0] * (N + 1)
    for i in range(M):
        p, S = input().split()
        p = int(p)
        if S == "AC":
            AC[p] = 1
        else:
            if AC[p] == 0:
                WA[p] += 1
    AC = sum(AC)
    WA = sum([WA[i] if AC[i] else 0 for i in range(1, N + 1)])
    print(AC, WA)
