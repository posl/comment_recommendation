def check(a):
    if a % 2 == 0 and (a % 3 == 0 or a % 5 == 0):
        return True
    else:
        return False
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if check(a[i]) == False:
        print("DENIED")
        exit()
print("APPROVED")
