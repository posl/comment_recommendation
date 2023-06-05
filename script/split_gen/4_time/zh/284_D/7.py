def prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
for i in range(int(input())):
    n = int(input())
    a = []
    for j in range(2, int(n**0.5)+1):
        if n % j == 0 and prime(j):
            a.append(j)
            a.append(n//j)
            break
    print(a[1], a[0])
