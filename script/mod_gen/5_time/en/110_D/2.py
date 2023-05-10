def divisors(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table.sort()
    return table
N, M = map(int, input().split())
MOD = 10**9 + 7
table = divisors(M)
ans = 0
for i in table:
    if M//i >= N:
        ans = max(ans, i)
print(ans)

if __name__ == '__main__':
    divisors()