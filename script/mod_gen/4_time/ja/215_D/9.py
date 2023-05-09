def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
l = [0]*(M+1)
for i in range(N):
    a = A[i]
    if a > M:
        break
    if l[a] != 0:
        continue
    for j in range(a,M+1,a):
        l[j] = 1
ans = []
for i in range(1,M+1):
    if l[i] == 0:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

if __name__ == '__main__':
    gcd()