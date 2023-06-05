def calc_sum(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum
num_list = []
N = int(input())
num_list = list(map(int, input().split()))
print(calc_sum(num_list))
