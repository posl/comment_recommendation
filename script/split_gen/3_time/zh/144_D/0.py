def main():
    a,b,x = map(int,input().split())
    if a*a*b/2 >= x:
        print(90 - 90*x/(a*a*b))
    else:
        print(90*x*2/(a*b*a) - 90)
