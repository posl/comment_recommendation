def main():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A.sort(reverse=True)
    A = [x for x in A if x != 1]
    S = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    D = [[0, 0] for _ in range(N+1)]
    for i in range(1, N+1):
        for a in A:
            if i - S[a] >= 0 and D[i-S[a]][0] + 1 > D[i][0]:
                D[i] = [D[i-S[a]][0] + 1, a]
    ans = ''
    i = N
    while i > 0:
        ans += str(D[i][1])
        i -= S[D[i][1]]
    print(ans)
