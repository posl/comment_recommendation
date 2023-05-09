def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    table.sort()
    return table
N = int(input())
ans = 0
for i in range(1,N+1,2):
    if len(divisor(i))==8:
        ans += 1
print(ans)
