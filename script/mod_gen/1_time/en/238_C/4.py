def f(n):
    if n==0:
        return 0
    if n<10:
        return sum(range(1,n+1))
    d=len(str(n))
    ans=0
    for i in range(1,d):
        ans+=45*10**(i-1)*i
    ans+=f(n%10**(d-1))
    ans+=sum(range(1,n//10**(d-1)+1))*d
    return ans
N=int(input())
print(f(N)%998244353)

if __name__ == '__main__':
    f()