def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    xy.sort()
    #print(xy)
    ans = 1
    for i in range(n-1):
        if xy[i][0] == xy[i+1][0]:
            if xy[i][1] != xy[i+1][1]:
                ans += 1
        elif xy[i][1] == xy[i+1][1]:
            if xy[i][0] != xy[i+1][0]:
                ans += 1
        else:
            ans += 1
    print(ans)
