def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab.sort()
    #print(ab)
    ans = 1
    num = 1
    for i in range(1,m):
        if ab[i-1][0] == ab[i][0]:
            if ab[i-1][1] != ab[i][1]:
                num += 1
                if num > ans:
                    ans = num
            else:
                pass
        else:
            num = 1
    print(ans)
