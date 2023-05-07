def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    D = {}
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            d = (x2-x1, y2-y1)
            if d in D:
                D[d] += 1
            else:
                D[d] = 1
    ans = N-1
    for v in D.values():
        ans = min(ans, N-v)
    print(ans)
