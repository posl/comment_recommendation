def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    for i in range(M):
        p[i], S[i] = input().split()
        p[i] = int(p[i])
    ans = [0] * N
    for i in range(M):
        if ans[p[i]-1] == 0 and S[i] == "AC":
            ans[p[i]-1] = i+1
    cnt = 0
    for i in range(N):
        if ans[i] != 0:
            cnt += 1
    ans2 = 0
    for i in range(M):
        if ans[p[i]-1] == i+1 and S[i] == "WA":
            ans2 += 1
    print(cnt, ans2)
