def check(n):
    if n % 2 == 0:
        if n % 3 == 0 or n % 5 == 0:
            return True
    return False
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if not check(i):
        print("DENIED")
        exit()
print("APPROVED")
