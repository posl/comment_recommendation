def main():
    a,b,x = map(int,input().split())
    s = x/a
    if 2*s >= a*b:
        print(90-2*(a*b-x)/(a**3))
    else:
        print(2*s/b)
