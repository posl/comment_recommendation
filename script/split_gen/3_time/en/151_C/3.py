def main():
    N, M = map(int, input().split())
    AC = [0 for _ in range(N)]
    WA = [0 for _ in range(N)]
    for _ in range(M):
        p, S = input().split()
        p = int(p)-1
        if AC[p] == 0:
            if S == "AC":
                AC[p] = 1
            else:
                WA[p] += 1
    AC = sum(AC)
    WA = sum([WA[i] for i in range(N) if AC[i] == 1])
    print(AC, WA)
