def sum(n):
    return n * (n + 1) // 2
n = int(input())
sum = 0
for i in range(n):
    a,b = map(int, input().split())
    sum += sum(b) - sum(a - 1)
print(sum)
