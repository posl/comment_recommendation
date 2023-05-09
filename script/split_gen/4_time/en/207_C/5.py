def main():
    n = int(input())
    tlr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        li, ri = tlr[i][1], tlr[i][2]
        for j in range(i+1, n):
            lj, rj = tlr[j][1], tlr[j][2]
            if (li <= lj and lj <= ri) or (li <= rj and rj <= ri) or (lj <= li and li <= rj) or (lj <= ri and ri <= rj):
                ans += 1
    print(ans)
