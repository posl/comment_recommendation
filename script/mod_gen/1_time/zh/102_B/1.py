def max_difference(a):
    max = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                if abs(a[i] - a[j]) > max:
                    max = abs(a[i] - a[j])
    return max
a = []
n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(max_difference(a))
