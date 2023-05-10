def main():
    a,b,c,d,e,f,x = map(int,input().split())
    t = 0
    aoki = 0
    takahashi = 0
    while(t<x):
        if(t%2==0):
            takahashi += a
        else:
            aoki += d
        t += 1
    if(takahashi > aoki):
        print("Takahashi")
    elif(takahashi < aoki):
        print("Aoki")
    else:
        print("Draw")
