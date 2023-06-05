def get_next_number(n):
    return a[n]
a = [int(i) for i in input().split()]
n = 0
for i in range(3):
    n = get_next_number(n)
print(n)
