def round_down(num, divisor):
    return num - (num%divisor)
X, K = map(int, input().split())
for i in range(K):
    X = round_down(X, 10**(i+1))
print(X)
