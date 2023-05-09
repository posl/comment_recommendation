def divisors(n):
    i = 1
    table = []
    while i*i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    table.sort()
    return table
N = int(input())
ans = divisors(N)
for i in ans:
    print(i)
