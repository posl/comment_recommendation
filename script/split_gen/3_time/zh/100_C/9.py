def count2(x):
    count = 0
    while x % 2 == 0:
        count += 1
        x = x // 2
    return count
n = int(input())
a = list(map(int, input().split()))
count = 0
for i in a:
    count += count2(i)
print(count)
