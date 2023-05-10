def input_to_int():
    return list(map(int,input().split()))
n,m = input_to_int()
a = input_to_int()
b = input_to_int()
a.sort()
b.sort()
j = 0
for i in range(n):
    if j == m:
        break
    if a[i] <= b[j]:
        j += 1
