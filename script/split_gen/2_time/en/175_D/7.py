def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p-1 for p in P]
    ans = -10**20
    for i in range(N):
        j = i
        cnt = 0
        tmp = 0
        while True:
            j = P[j]
            tmp += C[j]
            cnt += 1
            if j == i:
                break
        if tmp > 0:
            if K >= cnt:
                ans = max(ans, tmp*(K//cnt) + max(0, max(C)))
            else:
                ans = max(ans, max(C[:K]))
        else:
            ans = max(ans, max(C[:K]))
    print(ans)
