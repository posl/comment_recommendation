def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
N,X = map(int,input().split())
balls = []
for i in range(N):
    balls.append(list(map(int,input().split())))
ans = 0
for i in range(1,2**N):
    tmp = 1
    for j in range(N):
        if i>>j & 1:
            tmp *= balls[j][0]
    if X%tmp == 0:
        divisors = make_divisors(X//tmp)
        for divisor in divisors:
            if divisor <= balls[j][0]:
                ans += 1
print(ans)
