def max_sum(a):
    max_sum = a[0]
    current_sum = a[0]
    for i in range(1, len(a)):
        current_sum = max(current_sum + a[i], a[i])
        max_sum = max(current_sum, max_sum)
    return max_sum
n = int(input())
a = list(map(int, input().split()))
print(max_sum(a))
