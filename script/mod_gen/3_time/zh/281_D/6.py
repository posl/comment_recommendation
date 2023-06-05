def solve(n,k,d,a):
    if k==1:
        if a[0]%d==0:
            return -1
        else:
            return a[0]
    if k==n:
        sum=0
        for i in range(n):
            sum+=a[i]
        if sum%d==0:
            return -1
        else:
            return sum
    else:
        sum=0
        for i in range(n-k+1):
            for j in range(i+k-1,n):
                for t in range(i,j+1):
                    sum+=a[t]
                if sum%d==0:
                    sum=0
                    break
                else:
                    sum=0
            if sum==0:
                break
        return sum

if __name__ == '__main__':
    solve()