def XOR(a,b):
    a = bin(a)[2:]
    b = bin(b)[2:]
    if len(a)>len(b):
        b = '0'*(len(a)-len(b))+b
    else:
        a = '0'*(len(b)-len(a))+a
    c = ''
    for i in range(len(a)):
        if a[i]=='1' and b[i]=='1':
            c += '0'
        elif a[i]=='0' and b[i]=='0':
            c += '0'
        else:
            c += '1'
    return int(c,2)
N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans += XOR(A[i],A[j])
        ans %= mod
print(ans)
