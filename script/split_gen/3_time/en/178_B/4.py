def main():
    a,b,c,d = map(int,input().split())
    if a*b < c*d:
        print(c*d)
    elif a*b > c*d:
        print(a*b)
    else:
        print(a*b)
