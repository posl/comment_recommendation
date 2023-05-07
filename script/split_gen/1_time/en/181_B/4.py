def sum_natural_numbers(n):
    return (n*(n+1))//2
n = int(input())
sum = 0
for i in range(n):
    a,b = map(int,input().split())
    sum += sum_natural_numbers(b) - sum_natural_numbers(a-1)
print(sum)
