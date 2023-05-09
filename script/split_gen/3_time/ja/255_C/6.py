def main():
    x,a,d,n=map(int,input().split())
    if d>0:
        if x<=a:
            print(abs(x-a))
        elif x>=a+d*(n-1):
            print(abs(x-a-d*(n-1)))
        else:
            print(min(abs(x-a),abs(x-a-d*(n-1))))
    elif d==0:
        if x==a:
            print(0)
        else:
            print(abs(x-a))
    else:
        if x>=a:
            print(abs(x-a))
        elif x<=a+d*(n-1):
            print(abs(x-a-d*(n-1)))
        else:
            print(min(abs(x-a),abs(x-a-d*(n-1))))
