def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    while x > 0:
        if x >= a:
            taka += a * b
            x -= a
        else:
            taka += x * b
            x = 0
        if x >= d:
            aoki += d * e
            x -= d
        else:
            aoki += x * e
            x = 0
        if x >= c:
            x -=
