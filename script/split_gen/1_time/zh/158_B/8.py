def main():
    n,a,b = map(int,input().split())
    if a == 0:
        print(0)
    elif n <= a+b:
        print(a)
    else:
        print(a*(n//(a+b)) + min(a,n%(a+b)))
