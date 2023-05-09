def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    for i in range(M):
        p[i], S[i] = input().split()
        p[i] = int(p[i])
    ans = [0] * N
    for i in range(M):
        if S[i] == 'WA':
            ans[p[i]-1] -= 1
        else:
            ans[p[i]-1] = 10000
    ans = [a for a in ans if a > 0]
    print(len(ans), sum(ans))
