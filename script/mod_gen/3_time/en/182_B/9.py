def gcd(a,b):
    while a:
        a,b = b%a,a
    return b
N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(2,1001):
    cnt = 0
    for j in range(N):
        if A[j]%i == 0:
            cnt += 1
    if ans < cnt:
        ans = cnt
        ans2 = i
print(ans2)

if __name__ == '__main__':
    gcd()