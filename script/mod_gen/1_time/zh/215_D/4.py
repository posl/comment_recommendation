def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = list(set(A))
ans = 0
for i in range(1, M + 1):
    flag = True
    for j in range(len(A)):
        if gcd(A[j], i) != 1:
            flag = False
            break
    if flag:
        ans += 1
        print(i)
print(ans)

if __name__ == '__main__':
    gcd()