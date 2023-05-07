def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    if N == 1:
        for i in range(1, 17):
            T.append("_" * i + S[0])
        for i in range(1, 17):
            T.append(S[0] + "_" * i)
    else:
        for i in range(1, 17):
            T.append("_" * i + S[0])
        for i in range(1, 17):
            T.append(S[0] + "_" * i)
        for i in range(1, 17):
            T.append(S[1] + "_" * i)
        for i in range(1, 17):
            T.append("_" * i + S[1])
    T = set(T)
    ans = []
    for s in S:
        for t in T:
            if s in t:
                ans.append(t)
    ans = set(ans)
    if len(ans) == len(T):
        print(-1)
    else:
        print(list(T - ans)[0])
