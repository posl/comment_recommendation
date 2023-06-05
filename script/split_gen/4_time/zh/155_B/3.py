def check(x):
    if x % 2 == 0 and (x % 3 == 0 or x % 5 == 0):
        return True
    return False
n = int(input())
a = list(map(int, input().split()))
for x in a:
    if check(x) == False:
        print("DENIED")
        exit()
print("APPROVED")
