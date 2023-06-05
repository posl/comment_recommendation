def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i,n):
            x = x | a[j]
            ans = max(ans,x)
    print(ans)
main()
