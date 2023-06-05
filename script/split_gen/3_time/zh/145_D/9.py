def main():
    x,y = map(int,input().split())
    if (x+y)%3!=0:
        print(0)
        return
    n = (x+y)//3
    x = x-n
    y = y-n
    if x<0 or y<0:
        print(0)
        return
    if x>y:
        x,y = y,x
    ans = 1
    for i in range(x):
        ans = ans*(n-i)//(i+1)
    print(ans%1000000007)
