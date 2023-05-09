def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    #print(A)
    ans = 0
    for i in range(1,M+1):
        cnt = 0
        for j in range(N):
            if i in A[j][1:]:
                cnt += 1
        if cnt == N:
            ans += 1
    print(ans)
