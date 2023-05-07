def prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
a,b,c,d = map(int, input().split())
for i in range(a,b+1):
    for j in range(c,d+1):
        if prime(i+j):
            print("Aoki")
            exit()
print("Takahashi")
