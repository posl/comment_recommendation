def main():
    n,m,x,t,d = map(int,input().split())
    for i in range(x):
        t += d
    for i in range(x,n):
        t += d
    print(t)
