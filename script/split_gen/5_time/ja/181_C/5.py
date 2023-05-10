def main():
    # input
    N = int(input())
    XYs = []
    for _ in range(N):
        XYs.append(list(map(int, input().split())))
    # compute
    ans = 'No'
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = XYs[i]
                x2, y2 = XYs[j]
                x3, y3 = XYs[k]
                if (y2 - y1)*(x3 - x1) == (y3 - y1)*(x2 - x1):
                    ans = 'Yes'
    # output
    print(ans)
