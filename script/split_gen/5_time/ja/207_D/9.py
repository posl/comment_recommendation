def rotate(x, y, rad):
    return x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad)
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
T = [list(map(int, input().split())) for _ in range(N)]
for i in range(360):
    rad = i * math.pi / 180
    x, y = rotate(S[0][0], S[0][1], rad)
    dx = T[0][0] - x
    dy = T[0][1] - y
    ok = True
    for j in range(N):
        x, y = rotate(S[j][0], S[j][1], rad)
        if [x + dx, y + dy] not in T:
            ok = False
            break
    if ok:
        print('Yes')
        exit()
print('No')
