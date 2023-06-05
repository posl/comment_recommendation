def main():
    A,B,T=map(int,input().split())
    t=0
    for i in range(1,T+1):
        if i%A==0:
            t+=B
    print(t)
