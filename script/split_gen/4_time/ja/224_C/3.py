def main():
    N = int(input())
    XY = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                x1, y1 = XY[i]
                x2, y2 = XY[j]
                x3, y3 = XY[k]
                if x1 == x2:
                    if x2 == x3:
                        continue
                    else:
                        ans += 1
                        continue
                elif x2 == x3:
                    if x3 == x1:
                        continue
                    else:
                        ans += 1
                        continue
                elif x3 == x1:
                    if x1 == x2:
                        continue
                    else:
                        ans += 1
                        continue
                if y1 == y2:
                    if y2 == y3:
                        continue
                    else:
                        ans += 1
                        continue
                elif y2 == y3:
                    if y3 == y1:
                        continue
                    else:
                        ans += 1
                        continue
                elif y3 == y1:
                    if y1 == y2:
                        continue
                    else:
                        ans += 1
                        continue
                if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
                    continue
                else:
                    ans += 1
    print(ans)
