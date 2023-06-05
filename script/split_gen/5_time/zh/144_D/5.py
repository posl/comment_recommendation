def main():
    a,b,x = map(int, input().split())
    if x >= a*a*b/2:
        print(90 - 90*2*(a*a*b-x)/(a*a*a))
    else:
        print(90*2*x/(a*b*b))
