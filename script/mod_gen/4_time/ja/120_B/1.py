def divisors(n):
    i = 1
    table = []
    while i*i <= n:
        if n%i == 0:
            table.append(i)
            if i != n//i:
                table.append(n//i)
        i += 1
    table.sort()
    return table
a, b, k = map(int, input().split())
table = divisors(a)
table.extend(divisors(b))
table = sorted(set(table), reverse=True)
print(table[k-1])

if __name__ == '__main__':
    divisors()