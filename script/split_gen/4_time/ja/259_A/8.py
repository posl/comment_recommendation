def main():
    n,m,x,t,d = map(int,input().split())
    if m >= x:
        for i in range(m-x):
            t += d
    else:
        for i in range(x-m):
            t -= d
    print(t)
