def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
ans = 0
ans_num = 0
for k in range(2, 1001):
    cnt = 0
    for i in range(N):
        if A[i] % k == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        ans_num = k
print(ans_num)

if __name__ == '__main__':
    gcd()