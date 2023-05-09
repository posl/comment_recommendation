def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)
p = int(input())
c = 0
for i in range(10, 0, -1):
    c += p // fac(i)
    p = p % fac(i)
print(c)

if __name__ == '__main__':
    fac()