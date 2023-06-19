def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    ans = -1
    for i in range(1,n+1):
        if i == 1:
            ans = a[i-1]
        else:
            ans = ans + a[i-1]
    print(ans)
