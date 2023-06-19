def main():
    n,a,b = map(int,input().split())
    if a == 0:
        print(0)
        return
    if a+b >= n:
        print(a)
    else:
        print(a*(n//(a+b))+min(a,n%(a+b)))
