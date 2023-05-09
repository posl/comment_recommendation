def divisors(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            if i != n // i:
                table.append(n//i)
        i += 1
    return table
n = int(input())
ans = divisors(n)
ans.sort()
for i in ans:
    print(i)
