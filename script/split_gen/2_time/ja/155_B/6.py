def check(n):
    if (n % 2 == 0 and (n % 3 == 0 or n % 5 == 0)):
        return True
    else:
        return False
n = int(input())
a = list(map(int, input().split()))
flag = True
for i in range(n):
    if not check(a[i]):
        flag = False
        break
