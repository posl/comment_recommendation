def abs_sum(a,b,c):
    return abs(a) + abs(b) + abs(c)
N, M = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(2**3):
    tmp = []
    for j in range(N):
        cnt = 0
        for k in range(3):
            if (i >> k) & 1:
                cnt += xyz[j][k]
            else:
                cnt -= xyz[j][k]
        tmp.append(cnt)
    tmp.sort(reverse=True)
    ans = max(ans, sum(tmp[:M]))
print(ans)
