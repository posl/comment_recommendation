def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = [0]*(m+1)
for i in range(n):
    for j in range(1,m//a[i]+1):
        b[a[i]*j] += 1
ans = []
for i in range(1,m+1):
    if b[i] == 0:
        ans.append(i)
    else:
        pass
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

if __name__ == '__main__':
    gcd()