def nCr(n,r):
    import math
    f = math.factorial
    return f(n) / f(r) / f(n-r)
A,B,K = map(int,input().split())
ans = ''
while A>0 and B>0:
    if K > nCr(A+B-1,A-1):
        ans += 'b'
        B -= 1
        K -= nCr(A+B,A)
    else:
        ans += 'a'
        A -= 1
print(ans+'a'*A+'b'*B)

if __name__ == '__main__':
    nCr()