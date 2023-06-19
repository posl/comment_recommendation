def main():
    n,t=map(int,input().split())
    l=[]
    for _ in range(n):
        c,t=map(int,input().split())
        if t<=t:
            l.append((c,t))
    if len(l)==0:
        print("TLE")
    else:
        print(min(l)[0])
