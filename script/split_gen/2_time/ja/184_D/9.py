def main():
    a,b,c = map(int,input().split())
    print(a*b*c/(a+b+c)/(a+b+c-1))
