def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    #print(S)
    #print(T)
    ans = ""
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if (S[i] + "_" + S[j]) not in T:
                ans = S[i] + "_" + S[j]
                break
            if ("_" + S[i] + "_" + S[j]) not in T:
                ans = "_" + S[i] + "_" + S[j]
                break
            if (S[i] + "_" + S[j] + "_") not in T:
                ans = S[i] + "_" + S[j] + "_"
                break
            if ("_" + S[i] + "_" + S[j] + "_") not in T:
                ans = "_" + S[i] + "_" + S[j] + "_"
                break
        if ans != "":
            break
    print(ans)
