def sum(a):
    total = 0
    for i in range(len(a)):
        total = total + a[i]
    return total
n = int(input())
a = list(map(int, input().split()))
print(sum(a))
