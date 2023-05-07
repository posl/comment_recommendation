def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(3, 17):
        for j in range(N):
            if len(S[j]) > i:
                continue
            for k in range(N):
                if j == k:
                    continue
                if len(S[k]) > i - len(S[j]) - 1:
                    continue
                for l in range(N):
                    if j == l or k == l:
                        continue
                    if len(S[l]) > i - len(S[j]) - len(S[k]) - 2:
                        continue
                    for m in range(N):
                        if j == m or k == m or l == m:
                            continue
                        if len(S[m]) > i - len(S[j]) - len(S[k]) - len(S[l]) - 3:
                            continue
                        for n in range(N):
                            if j == n or k == n or l == n or m == n:
                                continue
                            if len(S[n]) > i - len(S[j]) - len(S[k]) - len(S[l]) - len(S[m]) - 4:
                                continue
                            for o in range(N):
                                if j == o or k == o or l == o or m == o or n == o:
                                    continue
                                if len(S[o]) > i - len(S[j]) - len(S[k]) - len(S[l]) - len(S[m]) - len(S[n]) - 5:
                                    continue
                                for p in range(N):
                                    if j == p or k == p or l == p or m == p or n == p or o == p:
                                        continue
                                    if len(S[p]) > i - len(S[j]) - len(S[k]) - len(S[l]) - len(S[m]) - len(S[n]) - len(S[o]) - 6:
                                        continue
                                    for q in range(N):
                                        if j == q or k == q or l == q or m == q or n == q or o == q or p == q:
                                            continue
                                        if len(S[q]) > i - len(S[j]) - len(S[k]) - len(S[l]) - len(S[m]) - len(S[n]) - len(S[o]) - len(S

if __name__ == '__main__':
    solve()