def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table
n = int(input())
table = divisor(n)
table.sort()
for i in range(len(table)):
    print(table[i])

if __name__ == '__main__':
    divisor()