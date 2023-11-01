def run():
    a,b,c,d,e,f,x = map(int, input().split())
    takahashi = 0
    aoki = 0
    for i in range(1, x+1):
        if i % (a + b) <= a:
            takahashi += 1
        if i % (d + e) <= d:
            aoki
