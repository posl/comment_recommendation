def isSGS(n):
    n = str(n)
    if '7' in n and '5' in n and '3' in n:
        return True
    else:
        return False
n = int(input())
count = 0
for i in range(1, n+1):
    if isSGS(i):
        count += 1
print(count)
