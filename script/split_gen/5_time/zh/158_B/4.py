def main():
    n,a,b = map(int,input().split())
    c = a+b
    if n%c == 0:
        print(a*(n//c))
    else:
        if n%c <= a:
            print(a*(n//c)+n%c)
        else:
            print(a*(n//c)+a)
