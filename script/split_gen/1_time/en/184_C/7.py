def main():
    r1,c1=map(int,input().split())
    r2,c2=map(int,input().split())
    print(min(abs(r1-r2)+abs(c1-c2),abs((r1-c1)-(r2-c2)),abs((r1+c1)-(r2+c2))//2))
