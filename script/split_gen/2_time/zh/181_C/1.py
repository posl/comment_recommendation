def getSum(a, b):
    return (a + b) * (b - a + 1) // 2
n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += getSum(a, b)
print(sum)
