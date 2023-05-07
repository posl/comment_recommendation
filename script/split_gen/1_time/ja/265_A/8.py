def main():
    x,y,n = map(int,input().split())
    print(n*x if n%2==1 else n*y if n%3==0 else n//3*y+(n%3)*x)
