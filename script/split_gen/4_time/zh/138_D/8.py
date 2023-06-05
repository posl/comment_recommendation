def main():
    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    px = [list(map(int, input().split())) for _ in range(q)]
    #print(ab, px)
    #print(n, q)
    #print(px[0][0])
    #print(ab[0][0])
    #print(ab[0][1])
    #print(px[0][1])
    #print(px[1][1])
    #print(px[2][1])
    #print(px[3][1])
    #print(px[4][1])
    #print(px[5][1])
    #print(px[6][1])
    #print(px[7][1])
    #print(px[8][1])
    #print(px[9][1])
    ans = [0] * n
    for i in range(q):
        ans[px[i][0]-1] += px[i][1]
    #print(ans)
    for i in range(n-1):
        if ab[i][0] == 1:
            ans[ab[i][1]-1] += ans[ab[i][0]-1]
        else:
            ans[ab[i][0]-1] += ans[ab[i][1]-1]
    print(*ans)
