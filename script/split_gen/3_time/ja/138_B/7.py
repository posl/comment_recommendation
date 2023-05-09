def calc_inverse_sum(n, list):
    sum = 0
    for i in range(n):
        sum += 1 / list[i]
    return 1 / sum
n = int(input())
list = list(map(int, input().split()))
print(calc_inverse_sum(n, list))
