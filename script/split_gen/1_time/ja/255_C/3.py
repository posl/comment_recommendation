def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(abs(x-a))
    else:
        if x == a:
            print(0)
        elif x < a:
            if d > 0:
                print(abs(a-x))
            else:
                if (a-x)%d == 0:
                    print(0)
                else:
                    print((a-x)%d)
        else:
            if d < 0:
                print(abs(a-x))
            else:
                if (x-a)%d == 0:
                    print(0)
                else:
                    print(d-(x-a)%d)
