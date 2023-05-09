def main():
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        t, d = map(int, input().split())
        T.append((d, t))
    T.sort(reverse=True)
    S = set()
    S.add(T[0][1])
    ans = T[0][0]
    for i in range(1, K):
        ans += T[i][0]
        S.add(T[i][1])
    ans += len(S) * len(S)
    for i in range(K, N):
        if T[i][1] in S:
            continue
        tmp = ans
        tmp -= T[K-1][0]
        tmp += T[i][0]
        tmp -= len(S) * len(S)
        tmp += (len(S) + 1) * (len(S) + 1)
        if tmp > ans:
            ans = tmp
            S.add(T[i][1])
        else:
            break
    print(ans)
