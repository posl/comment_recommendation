def get_divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            if i != n // i:
                table.append(n // i)
        i += 1
    table.sort()
    return table
n = int(input())
div = get_divisor(n)
for i in div:
    print(i)

if __name__ == '__main__':
    get_divisor()