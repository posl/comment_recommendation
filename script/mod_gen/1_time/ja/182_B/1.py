def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(2, 1001):
    cnt = 0
    for a in A:
        if a % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        ans_i = i
print(ans_i)

if __name__ == '__main__':
    gcd()