def main():
    n = int(input())
    tlr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if tlr[i][1]<=tlr[j][1]<=tlr[i][2] or tlr[i][1]<=tlr[j][2]<=tlr[i][2] or tlr[j][1]<=tlr[i][1]<=tlr[j][2] or tlr[j][1]<=tlr[i][2]<=tlr[j][2]:
                ans += 1
    print(ans)
