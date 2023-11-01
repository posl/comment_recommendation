def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if taka + b > x:
            print("Takahashi")
            break
        taka += b
        if aoki + e > x:
            print("Aoki")
