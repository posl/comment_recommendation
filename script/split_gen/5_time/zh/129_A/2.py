def main():
    p,q,r = map(int,input().split())
    print(min(p+q,min(q+r,r+p)))
