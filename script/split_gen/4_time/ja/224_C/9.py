def main():
    import sys
    readline = sys.stdin.buffer.readline
    N = int(readline())
    XY = [list(map(int,readline().split())) for _ in range(N)]
    XY.sort(key = lambda x:x[0])
    XY.sort(key = lambda x:x[1])
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                a = XY[i]
                b = XY[j]
                c = XY[k]
                if (b[0]-a[0])*(c[1]-a[1]) != (c[0]-a[0])*(b[1]-a[1]):
                    ans += 1
    print(ans)
