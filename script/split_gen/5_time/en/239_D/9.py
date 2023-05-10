def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): #nの平方根までの数で割り切れるか
        if n % i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
takahashi = 0
aoki = 0
for i in range(A, B+1):
    if prime(i):
        takahashi = i
        break
for i in range(C, D+1):
    if prime(i):
        aoki = i
        break
