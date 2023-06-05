def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if k==1:
        if a[0]%d==0:
            print(-1)
        else:
            print(a[0])
    else:
        sum = 0
        for i in range(n-k+1):
            for j in range(i+k-1,n):
                sum += a[j]
                if sum%d == 0:
                    sum = 0
                    break
            if sum!=0:
                break
        if sum == 0:
            print(-1)
        else:
            print(sum)
