def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if i == k or j == k:
                    continue
                for l in range(N):
                    if i == l or j == l or k == l:
                        continue
                    s = S[i] + "_" + S[j] + "_" + S[k] + "_" + S[l]
                    if len(s) < 3 or len(s) > 16:
                        continue
                    if s in T:
                        continue
                    print(s)
                    return
    print(-1)
