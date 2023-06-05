def S(n):
    m = str(n)
    sum = 0
    for i in range(len(m)):
        sum = sum + int(m[i])
    return sum
K = int(input())
n = 1
while K > 0:
    if S(n) * n <= S(n+1) * (n+1):
        print(n)
        K = K - 1
    n = n + 1
