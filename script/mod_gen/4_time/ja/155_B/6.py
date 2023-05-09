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
ans = 'APPROVED'
for i in a:
    if check(i) == False:
        ans = 'DENIED'
        break
print(ans)

if __name__ == '__main__':
    check()