def main():
    l1,r1,l2,r2=map(int,input().split())
    print(max(0,min(r1,r2)-max(l1,l2)))
