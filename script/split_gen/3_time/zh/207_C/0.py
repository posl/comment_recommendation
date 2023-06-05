def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                ans += 1
    print(ans)
