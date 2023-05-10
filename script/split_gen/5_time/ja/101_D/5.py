def s(n):
    return sum([int(i) for i in str(n)])
k = int(input())
n = 1
while k > 0:
    if n % s(n) == 0:
        print(n)
        k -= 1
    n += 1
