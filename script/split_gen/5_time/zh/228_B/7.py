def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a = [a[i]-1 for i in range(n)]
    ans = 1
    y = x-1
    while a[y]!=x-1:
        ans+=1
        y = a[y]
    print(ans)
