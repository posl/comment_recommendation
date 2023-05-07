def divisor(n):
    i = 1
    table = []
    while i*i <= n:
        if n%i == 0:
            table.append(i)
            if i != n//i:
                table.append(n//i)
        i += 1
    return table
N = int(input())
ans = 0
for i in range(1,N+1):
    ans += i*len(divisor(i))
print(ans)

if __name__ == '__main__':
    divisor()