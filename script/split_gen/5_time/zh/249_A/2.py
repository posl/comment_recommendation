def main():
    a,b,c,d,e,f,x = map(int,input().split())
    takahashi = 0
    aoki = 0
    for i in range(1,x+1):
        if i%a==0:
            takahashi += b
        if i%d==0:
            aoki += e
        if i%c==0:
            takahashi -= f
