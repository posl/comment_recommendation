def run():
    a,b,c,d,e,f,x=map(int,input().split())
    takahashi=0
    aoki=0
    while True:
        if x<=0:
            break
        x-=a
        if x<=0:
            takahashi+=x+a
            break
        x-=c
        takahashi+=a
        if x<=0:
            break
        x-=d
        if x<=0:
            aoki+=x+d
            bre

if __name__ == '__main__':
    run()