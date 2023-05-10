def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): # nの平方根まで調べれば十分
        if n%i == 0:
            return False
    return True
n = int(input())
ans = 0
for i in range(1, int(n**(1/4))+1):
    if n%i == 0:
        if is_prime(i) and is_prime(n//i**(3)):
            ans += 1
print(ans)

if __name__ == '__main__':
    is_prime()