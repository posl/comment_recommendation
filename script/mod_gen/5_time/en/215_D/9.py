def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
n,m = map(int, input().split())
a = list(map(int, input().split()))
t = [0]*(m+1)
for i in a:
    for j in range(1,m//i+1):
        t[i*j] = 1
ans = []
for i in range(1,m+1):
    if t[i] == 0:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)

if __name__ == '__main__':
    gcd()