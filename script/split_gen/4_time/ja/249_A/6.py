def main():
    a,b,c,d,e,f,x = map(int,input().split())
    #print(a,b,c,d,e,f,x)
    taka = 0
    aoki = 0
    for i in range(x):
        if i % (a+c) < a:
            taka += b
        if i % (d+e) < d:
            aoki += e
    if taka > aoki:
        print("Takahashi")
    elif taka < aoki:
        print("Aoki")
    else:
        print("Draw")
