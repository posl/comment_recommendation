def main():
    N = int(input())
    tlr = [[int(x) for x in input().split()] for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (tlr[i][1] <= tlr[j][1] <= tlr[i][2]) or (tlr[i][1] <= tlr[j][2] <= tlr[i][2]) or (tlr[j][1] <= tlr[i][1] <= tlr[j][2]) or (tlr[j][1] <= tlr[i][2] <= tlr[j][2]):
                ans += 1
    print(ans)
