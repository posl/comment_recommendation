def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        if taka + a > x:
            print("Takahashi")
            break
        taka += a
        if aoki + d > x:
            print("Aoki")
            break
        aoki += d
        if taka > aoki:
            aoki += e
        elif taka <
