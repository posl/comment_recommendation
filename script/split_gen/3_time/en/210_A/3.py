def main():
    n,a,x,y = map(int,input().split())
    total = 0
    for i in range(1,n+1):
        if i <= a:
            total += x
        else:
            total += y
    print(total)
