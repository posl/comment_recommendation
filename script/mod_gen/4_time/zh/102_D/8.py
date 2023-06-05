def main():
    n=int(input())
    a=list(map(int,input().split()))
    a_sum=[0]
    for i in range(n):
        a_sum.append(a_sum[i]+a[i])
    ans=10**9
    for i in range(1,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                p=a_sum[i]
                q=a_sum[j]-a_sum[i]
                r=a_sum[k]-a_sum[j]
                s=a_sum[n]-a_sum[k]
                max_num=max(p,q,r,s)
                min_num=min(p,q,r,s)
                ans=min(ans,max_num-min_num)
    print(ans)

if __name__ == '__main__':
    main()