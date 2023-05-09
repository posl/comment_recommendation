def check(num):
    while num > 0:
        if num % 10 == 7:
            return False
        num //= 10
    return True
N = int(input())
ans = 0
for num in range(1, N+1):
    if check(num) and check(int(oct(num))):
        ans += 1
print(ans)

if __name__ == '__main__':
    check()