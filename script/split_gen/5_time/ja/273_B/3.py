def get_digit(n):
    digit = 0
    while n > 0:
        n //= 10
        digit += 1
    return digit
X,K = map(int,input().split())
for _ in range(K):
    if X % 10 == 0:
        X //= 10
    else:
        X += 10 - X % 10
print(X)
