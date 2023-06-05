def getSum(start, end):
    return (start + end) * (end - start + 1) // 2
n = int(input())
sum = 0
for i in range(n):
    start, end = map(int, input().split())
    sum += getSum(start, end)
print(sum)
