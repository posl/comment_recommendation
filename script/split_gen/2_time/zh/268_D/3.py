def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i] == S[j]:
                print(-1)
                return
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
    for i in range(N):
        for j in range(M):
            if S[i] in T[j]:
                print(-1)
                return
    for i in range(M):
        for j in range(N):
            if T[i] in S[j]:
                print(-1)
                return
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if T[i] in T[j]:
                print(-1)
                return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i] in S[j]:
                print(-1)
                return
    if N == 1:
        print(S[0])
        return
    if M == 1:
        print(T[0])
        return
    for i in range(N):
        for j in range(M):
            if S[i][0] == T[j][-1]:
                print(T[j] + S[i])
                return
            if S[i][-1] == T[j][0]:
                print(S[i] + T[j])
                return
    for i in range(N):
        for j in range(M):
            for k in range(N):
                if i == k:
                    continue
                if S[i][-1] == S[k][0]:
                    for l in range(M):
                        if j == l:
                            continue
                        if S[k][-1] == T[l][0]:
                            print(S[i] + T[j] + S[k] + T[l])
                            return
                if S[i][0] == S[k][-1]:
                    for l in range(M):
