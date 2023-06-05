def main():
    x,y,n = map(int,input().split())
    print((n//3)*y + (n%3)*x)
