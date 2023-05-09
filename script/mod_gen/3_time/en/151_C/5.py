def main():
    N, M = [int(x) for x in input().split()]
    AC = [0] * N
    WA = [0] * N
    for i in range(M):
        p, S = input().split()
        p = int(p) - 1
        if S == "AC":
            AC[p] = 1
        elif S == "WA" and AC[p] == 0:
            WA[p] += 1
    AC = sum(AC)
    WA = sum([WA[i] for i in range(N) if AC[i] == 1])
    print(AC, WA)

if __name__ == '__main__':
    main()