def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if (x-a)%d == 0 and (x-a)//d >= 0:
            print((x-a)//d)
        else:
            print(1+min(abs(x-a)%d,abs(x-a+d)%d))