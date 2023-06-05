def problems151_c():
    N, M = map(int, input().split())
    ACs = [0] * N
    WAs = [0] * N
    for i in range(M):
        p, S = input().split()
        p = int(p)
        if S == 'AC':
            ACs[p-1] = 1
        else:
            if ACs[p-1] == 0:
                WAs[p-1] += 1
    print(sum(ACs), sum([ACs[i] * WAs[i] for i in range(N)]))

if __name__ == '__main__':
    problems151_c()