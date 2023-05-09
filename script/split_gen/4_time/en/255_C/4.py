def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x >= a:
            print(x-a)
        else:
            print(a-x)
    else:
        if n % 2 == 0:
            if x >= a:
                print(x-a)
            else:
                print(a-x)
        else:
            if x >= a:
                print(x-a-d)
            else:
                print(a-x+d)
