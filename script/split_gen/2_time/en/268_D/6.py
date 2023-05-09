def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    #print(N, M, S, T)
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if T[i] == T[j]:
                print(-1)
                return
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                print(-1)
                return
    #print('pass')
    for i in range(M):
        if T[i].count('_') == 0:
            continue
        for j in range(M):
            if i == j:
                continue
            if T[i].replace('_', '') == T[j]:
                print(-1)
                return
    #print('pass')
    for i in range(M):
        if T[i].count('_') == 0:
            continue
        for j in range(M):
            if i == j:
                continue
            if T[i].replace('_', '') in T[j]:
                print(-1)
                return
    #print('pass')
    for i in range(M):
        if T[i].count('_') == 0:
            continue
        for j in range(M):
            if i == j:
                continue
            if T[i].replace('_', '') in T[j].replace('_', ''):
                print(-1)
                return
    #print('pass')
    for i in range(M):
        if T[i].count('_') == 0:
            continue
        for j in range(M):
            if i == j:
                continue
            if T[i].replace('_', '') in T[j].replace('_', '') + T[j].replace('_', ''):
                print(-1)
                return
    #print('pass')
    #for i in range(M):
    #    if T[i].count('_') == 0:
    #        continue
    #    for j in range(M):
    #        if i == j:
    #            continue
    #        if T[i].replace('_', '') in T[j].replace('_', '') + T[j].replace('_', '') + T[j].replace('_', ''):
    #            print(-1)
    #            return
    #print('pass')
    for i in
