def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(m):
        a[-1]=a[-1]//2
        a.sort()
    print(sum(a))
