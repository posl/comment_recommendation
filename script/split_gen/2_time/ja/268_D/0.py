def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if k == i or k == j:
                    continue
                for l in range(N):
                    if l == i or l == j or l == k:
                        continue
                    X = S[i] + "_" + S[j] + "_" + S[k] + "_" + S[l]
                    X = X.replace("____", "_")
                    X = X.replace("___", "_")
                    X = X.replace("__", "_")
                    if len(X) < 4 or len(X) > 16:
                        continue
                    if X not in T:
                        print(X)
                        return
    print(-1)
