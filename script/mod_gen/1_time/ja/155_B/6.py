def check(n):
    if n % 2 == 0:
        if n % 3 == 0 or n % 5 == 0:
            return True
        else:
            return False
    else:
        return True
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if check(i) == False:
        print('DENIED')
        exit()
print('APPROVED')

if __name__ == '__main__':
    check()