def problems274_b():
    h,w = map(int,input().split())
    c = []
    for i in range(h):
        c.append(input())
    for i in range(w):
        cnt = 0
        for j in range(h):
            if c[j][i] == "#":
                cnt += 1
        print(cnt)
