def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    xy = [list(map(int,input().split())) for i in range(m)]
    #print(xy)
    for i in range(n-1):
        if a[i] >= xy[0][0]:
            a[i] += xy[0][1]
            xy.pop(0)
            if len(xy) == 0:
                break
        else:
            break
    #print(a)
    if a[-1] >= t:
        print('Yes')
    else:
        print('No')
