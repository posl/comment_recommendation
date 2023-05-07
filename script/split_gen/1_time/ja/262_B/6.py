def main():
    n,m = map(int,input().split())
    e = [list(map(int,input().split())) for _ in range(m)]
    e.sort()
    ans = 0
    for i in range(m):
        for j in range(i+1,m):
            if e[i][0] == e[j][0]:
                continue
            if e[i][1] == e[j][1]:
                continue
            if e[i][1] > e[j][0]:
                continue
            if e[i][1] < e[j][0] and e[j][1] > e[i][1]:
                ans += 1
    print(ans)
