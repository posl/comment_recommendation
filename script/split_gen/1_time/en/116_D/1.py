def main():
    N, K = map(int, input().split())
    T = [0] * N
    D = [0] * N
    for i in range(N):
        t, d = map(int, input().split())
        T[i] = t - 1
        D[i] = d
    D.sort(reverse=True)
    T.sort(reverse=True)
    T = list(set(T))
    T.sort()
    if len(T) <= K:
        print(sum(D))
        return
    ans = 0
    for i in range(K + 1):
        if i == 0:
            for j in range(K):
                ans += D[j]
            continue
        if i == K:
            for j in range(i):
                ans += D[j]
            continue
        if i == len(T):
            for j in range(i):
                ans += D[j]
            continue
        tmp = 0
        for j in range(i):
            tmp += D[j]
        for j in range(i):
            if T[j] == T[i]:
                for k in range(i, K):
                    tmp += D[k]
                break
        ans = max(ans, tmp)
    print(ans)
