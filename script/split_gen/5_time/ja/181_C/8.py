def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]
                if x1 == x2 and x1 == x3:
                    print('Yes')
                    return
                if x1 == x2:
                    continue
                if x2 == x3:
                    continue
                if x1 == x3:
                    continue
                if y1 == y2 and y1 == y3:
                    print('Yes')
                    return
                if y1 == y2:
                    continue
                if y2 == y3:
                    continue
                if y1 == y3:
                    continue
                if (x1-x2)/(y1-y2) == (x1-x3)/(y1-y3):
                    print('Yes')
                    return
    print('No')
