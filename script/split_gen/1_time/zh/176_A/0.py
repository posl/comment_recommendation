def main():
    n,x,t = map(int, input().split())
    print(int((n+x-1)/x*t))
