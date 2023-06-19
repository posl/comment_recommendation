def main():
    a,b,x=map(int,input().split())
    if x<=a*a*b/2:
        print(90-90*x/(a*a*b))
    else:
        print(90*x/(a*a*a)-90*a*b/(2*a*a*a-2*x))
