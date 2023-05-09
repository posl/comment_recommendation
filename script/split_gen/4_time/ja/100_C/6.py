def count_div2(x):
    count = 0
    while x%2 == 0:
        x = x/2
        count += 1
    return count
n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(n):
    count += count_div2(a[i])
print(count)
