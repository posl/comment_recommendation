def S(n):
    sum = 0
    while n>0:
        sum += n%10
        n = n//10
    return sum
K = int(input())
n = 1
while K>0:
    if S(n) == 1:
        print(n)
        K -= 1
    n += 1
