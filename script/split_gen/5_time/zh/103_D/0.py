def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab = sorted(ab,key=lambda x:x[1])
    ans = 1
    right = ab[0][1]
    for i in range(1,m):
        if ab[i][0] >= right:
            ans += 1
            right = ab[i][1]
    print(ans)
