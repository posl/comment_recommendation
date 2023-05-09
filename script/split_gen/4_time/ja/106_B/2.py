def check(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 8:
        return True
    else:
        return False
N = int(input())
count = 0
for i in range(1, N+1):
    if i % 2 == 1:
        if check(i) == True:
            count += 1
print(count)
