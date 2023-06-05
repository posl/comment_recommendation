def main():
    a,b,c = map(int,input().split())
    if a == b == c:
        print(1)
    else:
        print((a*b*c)/(a*b+b*c+c*a))
