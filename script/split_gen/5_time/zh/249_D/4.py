def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
N = int(input())
A = list(map(int, input().split()))
A.sort()
dict = {}
for i in range(N):
    if A[i] in dict:
        dict[A[i]] += 1
    else:
        dict[A[i]] = 1
ans = 0
for i in range(N):
    divisors = make_divisors(A[i])
    for j in range(len(divisors)):
        if divisors[j] in dict:
            ans += dict[divisors[j]]
            if A[i] == divisors[j]:
                ans -= 1
print(ans)
