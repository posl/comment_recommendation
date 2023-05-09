def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n = int(input())
a = list(map(int,input().split()))
left = [0] * (n + 1)
right = [0] * (n + 1)
for i in range(n):
    left[i+1] = gcd(left[i],a[i])
for i in range(n-1,-1,-1):
    right[i] = gcd(right[i+1],a[i])
ans = 1
for i in range(n):
    ans = max(ans,gcd(left[i],right[i+1]))
print(ans)

if __name__ == '__main__':
    gcd()