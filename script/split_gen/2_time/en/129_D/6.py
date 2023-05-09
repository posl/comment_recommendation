def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                cnt = 0
                ni,nj = i,j
                while 0<=ni<h and 0<=nj<w:
                    if s[ni][nj] == "#":
                        break
                    cnt += 1
                    ni += di
                    nj += dj
                ans = max(ans,cnt)
    print(ans)
main()
I'm not sure if this is the best way to do it, but it's the way I thought of. You can just check all the squares and see if you can light them up, and then you just take the max of all the squares you can light up. I think this is a O(n^3) solution, but I'm not sure.
