def main():
    n,x,t = map(int,input().split())
    print(t*((n+x-1)//x))
