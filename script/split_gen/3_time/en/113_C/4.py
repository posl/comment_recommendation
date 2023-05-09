def main():
    #input
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    #solve
    P = [P[i]-1 for i in range(M)]
    Y = [Y[i] for i in range(M)]
    pref = [[] for i in range(N)]
    for i in range(M):
        pref[P[i]].append(Y[i])
    for i in range(N):
        pref[i].sort()
    for i in range(M):
        j = pref[P[i]].index(Y[i])
        print('{:06d}'.format(P[i]+1) + '{:06d}'.format(j+1))
    #output
