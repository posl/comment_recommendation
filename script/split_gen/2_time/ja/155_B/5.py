def check(num):
    if num % 2 == 0:
        if num % 3 == 0 or num % 5 == 0:
            return True
    else:
        return False
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if check(i) == False:
        print('DENIED')
        exit()
print('APPROVED')
